__author__ = 'danidee'

from ui.ui_level import *

class level(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.level_ui = Ui_Level()
        self.level_ui.setupUi(self)

    @staticmethod
    def level_est(all_objects):
        for activity in all_objects:
            resource = activity.resource
            est = activity.est
            duration = activity.duration

            if est == 0:
                for count in range(int(duration)):
                    activity.level[0].append(resource)
            else:
                while len(activity.level[0]) < est:
                        activity.level[0].append(0)

                for count in range(int(duration)):
                    activity.level[0].append(resource)

    @staticmethod
    def level_lst(all_objects):
        for activity in all_objects:
            resource = activity.resource
            est = activity.est
            lst = activity.lst
            duration = activity.duration

            if est == lst:
                while len(activity.level[1]) < lst:
                    activity.level[1].append(0)

            elif est != lst:
                while len(activity.level[1]) < lst-1:
                    activity.level[1].append(0)

            for count in range(int(duration)):
                activity.level[1].append(resource)

        return all_objects

    @staticmethod
    def format_est_and_lst(nested_list):
        for i in nested_list:
            for count, j in enumerate(i):
                if j % 1 == 0.0:
                    i[count] = int(j)
        return nested_list

    def display_levelling_exercise(self, project_duration, all_objects, result, success, activity_level):
        if success == 'Yes':
            self.level_ui.estTable.setColumnCount(project_duration)
            self.level_ui.estTable.setRowCount(len(all_objects) + 1)
            self.level_ui.lstTable.setColumnCount(project_duration)
            self.level_ui.lstTable.setRowCount(len(all_objects) + 1)

            activity_id = [i.id for i in all_objects]
            rowCount = self.level_ui.estTable.rowCount()

            for row in range(rowCount -1):
                item = QtGui.QTableWidgetItem(str(activity_id[row]))
                self.level_ui.estTable.setVerticalHeaderItem(row, item)

            for row in range(rowCount - 1):
                item = QtGui.QTableWidgetItem(str(activity_id[row]))
                self.level_ui.lstTable.setVerticalHeaderItem(row, item)


            item = QtGui.QTableWidgetItem()
            self.level_ui.estTable.setVerticalHeaderItem(rowCount-1, item)
            self.level_ui.estTable.verticalHeaderItem(rowCount-1).setText('Total')

            item = QtGui.QTableWidgetItem()
            self.level_ui.lstTable.setVerticalHeaderItem(rowCount-1, item)
            self.level_ui.lstTable.verticalHeaderItem(rowCount-1).setText('Total')

            for row, activity in enumerate(activity_level):
                while len(activity[0]) < project_duration:
                    activity[0].append('0')
                for column, value in enumerate(activity[0]):
                    item = QtGui.QTableWidgetItem(str(value))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.level_ui.estTable.setItem(row, column, item)

            for column, value in enumerate(result[0]):
                item = QtGui.QTableWidgetItem(str(value))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                row = len(activity_level)
                self.level_ui.estTable.setItem(row, column, item)




            '''*****************For the LST Resource loading exercise****************'''

            for row, activity in enumerate(activity_level):
                while len(activity[1]) < project_duration:
                    activity[1].append('0')
                for column, value in enumerate(activity[1]):
                    item = QtGui.QTableWidgetItem(str(value))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.level_ui.lstTable.setItem(row, column, item)

            for column, value in enumerate(result[1]):
                item = QtGui.QTableWidgetItem(str(value))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                row = len(activity_level)
                self.level_ui.lstTable.setItem(row, column, item)

        self.show()


if __name__ == '__main__': main()
