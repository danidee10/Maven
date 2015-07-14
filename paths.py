__author__ = 'danidee'

import sys
from ui.ui_paths import *
from graph import *

class criticalPath(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(criticalPath, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculateButton.clicked.connect(self.find_paths)
        self.ui.clearButton.clicked.connect(self.ui.tableWidget.clearContents)
        #self.ui.networkDiagram.hide()

        #Initialize all the variables we're going to use to calculate the critical path
        self.id = None
        self.predecessor = tuple()
        self.duration = None
        self.est = None
        self.lst = None
        self.resource = None
        self.is_critical = 'No'
        self.all_objects = list()
        self.level = [[], []]

    def __lt__(self, other):
        return other.id > self.id

    def __gt__(self, other):
        return self.id > other.id

    def get_num_act(self):
        num_act, ok = QtGui.QInputDialog.getInteger(self, 'Input activity number', 'How many activities activities?:')

        if ok:
            self.initializeTable(num_act)
            if num_act == 0:
                sys.exit()
        else:
            sys.exit()

    def initializeTable(self, num_rows):
        self.ui.tableWidget.setRowCount(num_rows)

    def get_properties(self):
        all_activities = list()
        allRows = self.ui.tableWidget.rowCount()
        for row in range(0, allRows):
            activity = criticalPath()
            name = self.ui.tableWidget.item(row, 0)
            name = name.text()

            duration = self.ui.tableWidget.item(row, 3)
            duration = duration.text()

            predecessor = self.ui.tableWidget.item(row, 2)
            if predecessor is not None:
                predecessor = predecessor.text()
                predecessor = tuple(predecessor.replace(',', ''))
            else:
                predecessor = ('0',)

            resource = self.ui.tableWidget.item(row, 4)
            if resource is not None:
                resource = resource.text()

            while True:
                try:
                    duration = float(duration)
                    break
                except ValueError:
                    print('{} is not a number please enter a valid number\n'.format(duration))
                    continue

            if resource is not None:
                while True:
                    try:
                        resource = float(resource)
                        break
                    except ValueError:
                        print('{} is not a number please enter a valid number\n'.format(resource))
                        continue

            '''set the properties based on what was gotten from the user'''
            activity.set_properties(name, predecessor, duration, resource)
            all_activities.append(activity)

        return all_activities

    def set_properties(self, name, predecessor, duration, resource):
        self.id = name
        self.predecessor = predecessor
        self.duration = duration
        if resource is not None:
            self.resource = resource

    def get_starting_nodes(self, all_objects):
        '''gets the starting nodes/activities and puts them individually into a nested list'''
        starting_nodes = list()
        for i in all_objects:
            for a in i.predecessor:
                if '0' in a:
                    tmplist = list()
                    tmplist.append(i)
                    starting_nodes.append(tmplist)

        return starting_nodes

    def get_branches(self, starting_nodes, all_objects):
        '''
        Do a forward pass and checks all the activities individually and connects
        them to their matching predecessors
        '''

        for ind, st_nodes in enumerate(starting_nodes):
            for node in all_objects:
                if st_nodes[-1].id in node.predecessor:
                    starting_nodes[ind].append(node)

                    '''
                    If the length of a starting node is more than one check the second to the last activity
                    if it has other successors, if so then connect it to the matching predecessor
                    '''

                elif len(st_nodes) > 1:
                    if st_nodes[-2].id in node.predecessor:
                        new_path = list()
                        new_path.append(node)
                        starting_nodes.append(new_path)

        return starting_nodes

    def patch_branches(self, starting_nodes, all_objects):
        '''
        do a backward pass and patch all the nodes/activities which have not been connected to their predecessor
        from the previous calculation
        '''
        for ind, final_result in enumerate(starting_nodes):
                while final_result[0].predecessor != ('0',):
                    for node in all_objects:
                        if node.id in final_result[0].predecessor:
                            starting_nodes[ind].insert(0, node)

        '''
        for some reason i don't know duplicates are generated when calculating all the possible paths,
        this block of code removes all duplicates in the nested list, i will dive down into the code and
        fix this
        '''
        all_paths = list()
        for path in starting_nodes:
            if sorted(path) not in all_paths:
                all_paths.append(sorted(path))

        return all_paths

    def get_est(self, all_objects):
        '''checks all the activities and calculates the earliest starting time by using the forward pass'''
        for activity in all_objects:

            if '0' in activity.predecessor:
                activity.est = 0
            else:
                for pred in activity.predecessor:
                    for next_activity in all_objects:
                        if pred == next_activity.id and activity.est is not None:
                            value = next_activity.est + next_activity.duration
                            activity.est = max([activity.est, value])
                            activity.est = round(activity.est, 1)

                        if pred == next_activity.id and activity.est is None:
                            activity.est = next_activity.est + next_activity.duration
                            activity.est = round(activity.est, 1)

        print('Earliest starting time')
        for act in all_objects:
            print(act.id, act.est)

    def get_lst(self, all_objects, project_duration):
        '''
        method to calculate the latest starting time by reversing the
        list and doing a backward pass through all the activities
        '''
        all_objects.reverse()
        for activity in all_objects:
            for succ in activity.predecessor:
                for prev_activity in all_objects:
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
        all_objects.reverse()
        for act in all_objects:
            print(act.id, act.lst)

    def print_est_and_lst(self, all_objects):
        ests = [act.est for act in all_objects]
        lsts = [act.lst for act in all_objects]

        for count, est in enumerate(ests):
            if est % 1 == 0.0:
                est = int(est)
            newEST = QtGui.QTableWidgetItem(str(est))
            self.ui.tableWidget.setItem(count, 5, newEST)

        for count, lst in enumerate(lsts):
            if lst % 1 == 0.0:
                lst = int(lst)
            newLST = QtGui.QTableWidgetItem(str(lst))
            self.ui.tableWidget.setItem(count, 6, newLST)

    def find_paths(self):
        all_objects = self.get_properties()
        starting_nodes = self.get_starting_nodes(all_objects)

        #get all the possible paths in the project
        starting_nodes = self.get_branches(starting_nodes, all_objects)
        all_paths = self.patch_branches(starting_nodes, all_objects)

        #if all_path is not empty then print all the possible paths in the project
        if None != all_paths:
            print('The possible paths in the project are')
            for i in all_paths:
                print( '==>'.join(str(a.id) for a in i))

            critical_path = ([path for path in max(all_paths, key=lambda ls: sum(obj.duration for obj in ls))])
            visual_path = ( '==>'.join([str(a.id) for a in critical_path]))
            project_duration = ((max([sum([node.duration for node in object]) for object in all_paths])))

            print('The critical path is {} and the project duration is {}'.format(visual_path, project_duration))

            #calculate the est
            self.get_est(all_objects)

            #for all activities in the critical path make the est equal to the lst of the activity
            for activity in critical_path:
                activity.is_critical = 'Yes'

            for activity in all_objects:
                if activity.is_critical == 'Yes':
                    activity.lst = activity.est

            #calculate the lst
            self.get_lst(all_objects, project_duration)

            #display the result
            self.print_est_and_lst(all_objects)

            draw_g = draw_graph()
            draw_g.draw(all_objects, all_paths, critical_path)
        else:
            print('There was a problem calculating the critical path')


if __name__ == '__main__': main()
