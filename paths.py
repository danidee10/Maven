__author__ = 'danidee'

import sys
from itertools import zip_longest

from ui.ui_paths import *
from level import level
from graph import draw_graph


class Activity:
    """basic structure of an activity having an id, predecessor, duration and a resource"""

    def __init__(self, id, predecessor, duration, resource):
        self.id = id
        self.predecessor = predecessor
        self.duration = duration
        self.resource = resource if resource is not None else None
        self.est = None
        self.lst = None
        self.is_critical = 'No'
        self.level = [[], []]

    def __repr__(self):
        return self.id


class criticalPath(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculateButton.clicked.connect(self.find_paths)
        self.ui.clearButton.clicked.connect(self.ui.tableWidget.clearContents)
        self.ui.addRowButton.clicked.connect(self.addRow)
        self.ui.delRowButton.clicked.connect(self.delRow)
        self.ui.viewResourceButton.clicked.connect(lambda: self.display_rlevelling(self.all_activities))
        self.actionHelp = QtGui.QAction('Help', self, statusTip="Help and Docs", triggered=self.help)
        self.actionHelp.setObjectName("actionHelp")
        self.ui.menubar.addAction(self.actionHelp)
        self.actionAbout = QtGui.QAction('About', self, statusTip="About Maven", triggered=self.about)
        self.actionAbout.setObjectName("actionAbout")
        self.ui.menubar.addAction(self.actionAbout)

        self.all_activities = None # created because self.display_rlevelling can't access all the activities
        self.success = 'No'
        self.progress = 'Yes'

    def __lt__(self, other):
        return other.id > self.id

    def __gt__(self, other):
        return self.id > other.id
        
    def about(self):
        QtGui.QMessageBox.about(self, "About Maven", "Maven Version 1.0\nAuthor: Osaetin Daniel")

    def help(self):
        QtGui.QMessageBox.about(self, "Help and Docs", "Documentation is available online\nat www.github.com")

    def handle_errors(self, message, details):
        msgbox = QtGui.QMessageBox()
        msgbox.setWindowTitle('Error!')
        msgbox.setText(message)
        msgbox.setDetailedText(details)
        msgbox.setStyleSheet('background-color: rgb(63, 63, 63); color: #ffffff;')
        msgbox.exec()
        self.progress = 'No'

    def get_number_of_activities(self):
        while True:
            num_act, ok = QtGui.QInputDialog.getInteger(self, 'Input activity number', 'How many activities are involved?:')
            if ok:
                    if num_act < 2 :
                        self.handle_errors('{} is not a valid activity number'.format(num_act), 'Please enter a valid number')
                        continue
                    else:
                        self.initializeTable(num_act)
                        break
            else:
                sys.exit()

    def initializeTable(self, num_rows):
        self.ui.tableWidget.setRowCount(num_rows)

    def addRow(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

    def delRow(self):
        row = self.ui.tableWidget.rowCount()
        if row > 1:
            self.ui.tableWidget.removeRow(row - 1)

    def get_properties(self):
        all_activities = []  # reset self.activities when calling the method

        rowCount = self.ui.tableWidget.rowCount()
        for row in range(0, rowCount):
            name = self.ui.tableWidget.item(row, 0)

            if name is not None:
                name = name.text()
                if name == '':
                    error = 'activity id cannot be empty'
                    details = 'please enter a value for the empty activity at row {}'.format(row+1)
                    self.handle_errors(error, details)
                else:
                    self.progress = 'Yes'
            else:
                error = 'activity id cannot be empty'
                details = 'please enter a value for the empty activity id  at row {}'.format(row+1)
                self.handle_errors(error, details)

            predecessor = self.ui.tableWidget.item(row, 2)
            if predecessor is not None:
                predecessor = predecessor.text()
                if predecessor == '':
                    predecessor = ('0',)
                else:
                    predecessor = tuple(predecessor.replace(',', ''))
            else:
                predecessor = ('0',)

            duration = self.ui.tableWidget.item(row, 3)
            if duration is not None:
                duration = duration.text()
                if duration == '':
                    error = 'duration cannot be empty'
                    details = 'please enter a value for the activity duration at row {}'.format(row+1)
                    duration = None
                    self.handle_errors(error, details)
            else:
                error = 'duration cannot be empty'
                details = 'please enter a value for the activity duration at row {}'.format(row +1)
                self.handle_errors(error, details)

            resource = self.ui.tableWidget.item(row, 4)
            if resource is not None:
                resource = resource.text()
                if resource == '':
                    resource = None

            if duration is not None:
                try:
                    duration = float(duration)
                except ValueError:
                    message = '{} is not a valid duration please input a number\n'.format(duration)
                    details = 'you entered a character which is not a number, The duration is supposed to be a number'
                    self.handle_errors(message, details)

            if resource is not None:
                try:
                    resource = float(resource)
                except ValueError:
                    message = '{} is not a valid resource please input a number\n'.format(resource)
                    details = 'you entered a character which is not a number, The resource is supposed to be a number'
                    self.handle_errors(message, details)

            '''set the properties based on what was gotten from the user'''
            activity = Activity(name, predecessor, duration, resource)
            all_activities.append(activity)

        return all_activities

    def get_starting_nodes(self, all_activities):
        """
        :param all_activities: all activities in the project e.g
                                +----------------+---------------+
                                | Activity id    | Predecessor   |
                                +----------------+---------------|
                                | A              | -             |
                                | B              | -             |
                                | C              | A             |
                                | D              | A             |
                                | E              | B             |
                                +----------------+---------------+

        :return: activities with no predecessor = [A, B]
        """
        starting_nodes = list()
        for i in all_activities:
            for a in i.predecessor:
                if '0' in a:
                    starting_nodes.append(i)

        return starting_nodes

    def build_graph(self, all_activities, starting_nodes, result):
        """
        Recursive function that finds all the possible paths in the project, by using the activity predecessors to
        match parents to their child nodes
        :param all_activities: all activities in the project
        :param starting_nodes: activities without predecessors = [A, B]
        :param result: nested form of starting nodes = [[A, B]]
        :return: all the possible paths in the project
        """
        node_found = False
        for count, st_nodes in enumerate(starting_nodes):
            for node in all_activities:
                if st_nodes.id in node.predecessor:  # a node was found process it (add the node to it's predecessor)
                    node_found = True
                    if st_nodes.id != result[count][-1].id:
                        tmplist = result[count][:-1]
                        tmplist.append(node)
                        result.append(tmplist)
                    else:
                        result[count].append(node)

        if node_found:
            starting_nodes = list()
            for i in result:
                starting_nodes.append(i[-1])
            return self.build_graph(all_activities, starting_nodes, result)
        else:
            return result

    def get_est(self, all_activities):
        """
        caluclates the earliest starting time of all activities in the project (Forward)
        :param all_activities: All activities in the project
        :return: None
        """
        for activity in all_activities:

            if '0' in activity.predecessor:
                activity.est = 0
            else:
                for pred in activity.predecessor:
                    for next_activity in all_activities:
                        try:
                            if pred == next_activity.id and activity.est is not None:
                                value = next_activity.est + next_activity.duration
                                activity.est = max([activity.est, value])
                                activity.est = round(activity.est, 1)

                            if pred == next_activity.id and activity.est is None:
                                activity.est = next_activity.est + next_activity.duration
                                activity.est = round(activity.est, 1)

                        except TypeError:
                                self.handle_errors('Problem calculating the est', 'there was a problem calculating the est please check your predecessors column for non-existing predecessors also the network diagram might not look correct')

        print('Earliest starting time')
        for act in all_activities:
            print(act.id, act.est)

    def get_lst(self, all_activities, project_duration):
        """
        calculates the latest starting time by reversing the list and looping through it (Backward pass)
        :param all_activities: All activities in the project
        :param project_duration: Total duration of the project
        :return: None
        """

        all_activities.reverse()
        for activity in all_activities:
            for succ in activity.predecessor:
                for prev_activity in all_activities:
                    if activity.lst is not None:
                        if succ == prev_activity.id and prev_activity.lst is not None:
                            value = activity.lst - prev_activity.duration
                            prev_activity.lst = min([prev_activity.lst, value])
                            prev_activity.lst = round(prev_activity.lst, 1)

                        if succ == prev_activity.id and prev_activity.lst is None:
                            prev_activity.lst = activity.lst - prev_activity.duration
                            prev_activity.lst = round(prev_activity.lst, 1)
                    else:
                        activity.lst = project_duration - activity.duration
                        prev_activity.lst = round(prev_activity.lst, 1)

        print('Latest starting time')
        all_activities.reverse()
        for act in all_activities:
            print(act.id, act.lst)

    def format_ests_and_lsts(self, all_activities):
        """
        Converts all the est's and lst's of all activities in the project to strings because QTableWidget can only
        display strings
        :param all_activities: All activities in the project
        :return: None
        """
        ests = [act.est for act in all_activities]
        lsts = [act.lst for act in all_activities]

        for count, (est, lst) in enumerate(zip(ests, lsts)):
            if est % 1 == 0.0:
                est_string = QtGui.QTableWidgetItem(str(int(est)))
                self.ui.tableWidget.setItem(count, 5, est_string)

            if lst % 1 == 0.0:
                lst_string = QtGui.QTableWidgetItem(str(int(lst)))
                self.ui.tableWidget.setItem(count, 6, lst_string)

    def display_graph_and_labels(self, visual_path, project_duration):
        self.ui.scrollArea.setStyleSheet('background-color: #ffffff')
        self.ui.criticalPathLabel.setWordWrap(True)
        self.ui.projectDurationLabel.setWordWrap(True)
        networkPixmap = QtGui.QPixmap('graphs/network_diagram.png')
        self.ui.networkDiagram.setPixmap(networkPixmap)
        self.ui.criticalPathLabel.setText(visual_path)
        self.ui.projectDurationLabel.setText('The total duration of the project is {}'.format(int(project_duration)))

    def format_est_and_lst(self, nested_list):
        for i in nested_list:
            for count, j in enumerate(i):
                try:
                    if j % 1 == 0.0:
                        i[count] = int(j)
                except TypeError:
                    pass
        return nested_list

    def find_paths(self):

        all_activities = self.get_properties()  # gets all the activities and puts them into self.all_activities
        if self.progress == 'Yes':
            starting_nodes = self.get_starting_nodes(all_activities)

            # get all the possible paths in the project
            result = [starting_nodes[:]]
            all_paths = self.build_graph(all_activities, starting_nodes, result)

            # if all_path is not empty then print all the possible paths in the project
            if None != all_paths:
                print('The possible paths in the project are')
                for i in all_paths:
                    print( '==>'.join(str(a.id) for a in i))

                critical_path = ([path for path in max(all_paths, key=lambda ls: sum(obj.duration for obj in ls))])
                visual_path = (','.join([str(a.id) for a in critical_path]))
                self.project_duration = ((max([sum([node.duration for node in object]) for object in all_paths])))

                visual_path = 'The critical path is: {}'.format(visual_path)

                # calculate and set the est for each activity
                self.get_est(all_activities)

                # for all activities in the critical path make the est equal to the lst of the activity
                for activity in critical_path:
                    activity.is_critical = 'Yes'
                    activity.lst = activity.est # est and lst are equal for activities on the critical path

                # calculate and set the lst for each activity
                self.get_lst(all_activities, self.project_duration)

                # format the est and lst so it can be displayed to the user
                self.format_ests_and_lsts(all_activities)

                draw_g = draw_graph()
                draw_g.draw(all_activities, all_paths, critical_path)

                self.display_graph_and_labels(visual_path, self.project_duration)
            else:
                print('There was a problem calculating the critical path')

            '''*********************All the calculations for the resource levelling class*******************'''

            ''' Test to make sure all the resource values are entered in the table
            before proceeding by using a counter variable'''

            counter = 0

            for act in all_activities:
                if act.resource is not None:
                    counter = counter + 1

            if counter == len(all_activities):
                self.resourcelevel = level()
                self.resourcelevel.level_est(all_activities)
                self.all_objects = self.resourcelevel.level_lst(all_activities)

                # list comprehension to add all the values in the est and lst of the objects
                self.result = [[sum(j) for j in zip_longest(*i, fillvalue=0)] for i in zip_longest(*[activity.level for activity in all_activities], fillvalue=[0])]
                self.result = self.format_est_and_lst(self.result)

                for i in self.result:
                    print(i)

                maxvalue = [max(i) for i in self.result]
                maxvalue = max(maxvalue)

                total = [[sum(j)] for j in [i for i in self.result]]
                total = self.format_est_and_lst(total)
                print(total)
                b = [max(i) for i in total]
                b = max(b)
                a = maxvalue * self.project_duration
                efficiency = ('The efficiency is {0:.1f} percent'.format(b/a * 100))
                print(efficiency)
                self.ui.efficiencyTitle.setText('EFFICIENCY')
                self.ui.efficiencyLabel.setText(efficiency)
                self.success = 'Yes'
                self.all_activities = all_activities[:] # create self.all_activities only when other calculations have been done
            elif counter < len(all_activities) and counter != 0:
                self.handle_errors('empty resource values', 'Make sure all the resource values are set before proceeding')

    def display_rlevelling(self, all_activities):
        if self.success == 'Yes':
            activity_level = [i.level for i in self.all_activities]
            for row, activity in enumerate(activity_level):
                self.format_est_and_lst(activity)
            self.resourcelevel.display_levelling_exercise(self.project_duration, self.all_activities, self.result, self.success, activity_level)

if __name__ == '__main__':
    main()
