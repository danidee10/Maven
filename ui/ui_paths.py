__author__ = 'danidee'

import sys

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 726)
        MainWindow.setMinimumSize(QtCore.QSize(1015, 726))
        MainWindow.setMaximumSize(QtCore.QSize(1015, 726))
        MainWindow.setStyleSheet("background-color: rgb(63, 63, 63); color: #ffffff;")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(760, 10, 111, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addRowButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.addRowButton.setFont(font)
        self.addRowButton.setStyleSheet("color: #ffffff; background-color: rgb(85, 170, 0); border: 1px solid rgb(85, 170, 0); padding: 5px; height: 80px;")
        self.addRowButton.setObjectName("addRowButton")
        self.verticalLayout.addWidget(self.addRowButton)
        self.calculateButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.calculateButton.setFont(font)
        self.calculateButton.setStyleSheet("background-color: rgb(85, 170, 0); color: #ffffff; border: 1px solid rgb(85, 170, 0); padding: 5px; height: 80px;")
        self.calculateButton.setObjectName("calculateButton")
        self.verticalLayout.addWidget(self.calculateButton)
        self.clearButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("color: #ffffff; background-color:  tomato; border: 1px solid tomato; padding: 5px; height: 80px;")
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout.addWidget(self.clearButton)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 740, 301))
        self.tableWidget.setMaximumSize(QtCore.QSize(740, 301))
        self.tableWidget.setStyleSheet("background-color: #ffffff; color: #666;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(880, 10, 113, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.loadESTButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.loadESTButton.setFont(font)
        self.loadESTButton.setStyleSheet("background-color: rgb(85, 0, 255); color: #ffffff; border: 1px solid rgb(85, 0, 255); padding: 5px; height: 80px;")
        self.loadESTButton.setObjectName("loadESTButton")
        self.verticalLayout_2.addWidget(self.loadESTButton)
        self.loadLSTButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.loadLSTButton.setFont(font)
        self.loadLSTButton.setStyleSheet("color: #ffffff; background-color: rgb(85, 170, 0); border: 1px solid rgb(85, 170, 0); padding: 5px; height: 80px;")
        self.loadLSTButton.setObjectName("loadLSTButton")
        self.verticalLayout_2.addWidget(self.loadLSTButton)
        self.efficiencyButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.efficiencyButton.setFont(font)
        self.efficiencyButton.setStyleSheet("background-color: rgb(85, 0, 255); color: #ffffff; border: 1px solid rgb(85, 0, 255);  padding: 5px; height: 80px;")
        self.efficiencyButton.setObjectName("efficiencyButton")
        self.verticalLayout_2.addWidget(self.efficiencyButton)
        self.resultWidget = QtGui.QFrame(self.centralwidget)
        self.resultWidget.setGeometry(QtCore.QRect(740, 320, 261, 341))
        self.resultWidget.setStyleSheet("border: 4px double #ffffff; color: #ffffff;")
        self.resultWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.resultWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.resultWidget.setObjectName("resultWidget")
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 319, 721, 341))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.networkDialog = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.networkDialog.setContentsMargins(0, 0, 0, 0)
        self.networkDialog.setObjectName("networkDialog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile_Open = QtGui.QMenu(self.menubar)
        self.menuFile_Open.setObjectName("menuFile_Open")
        self.menuHere = QtGui.QMenu(self.menubar)
        self.menuHere.setObjectName("menuHere")
        self.menuQuit = QtGui.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen_2 = QtGui.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.menuFile_Open.addAction(self.actionOpen)
        self.menuFile_Open.addAction(self.actionSave)
        self.menuFile_Open.addAction(self.actionOpen_2)
        self.menubar.addAction(self.menuFile_Open.menuAction())
        self.menubar.addAction(self.menuHere.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.addRowButton, self.calculateButton)
        MainWindow.setTabOrder(self.calculateButton, self.clearButton)
        MainWindow.setTabOrder(self.clearButton, self.loadESTButton)
        MainWindow.setTabOrder(self.loadESTButton, self.loadLSTButton)
        MainWindow.setTabOrder(self.loadLSTButton, self.efficiencyButton)
        MainWindow.setTabOrder(self.efficiencyButton, self.tableWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.addRowButton.setText(QtGui.QApplication.translate("MainWindow", "Add Row", None, QtGui.QApplication.UnicodeUTF8))
        self.calculateButton.setText(QtGui.QApplication.translate("MainWindow", "Calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Id", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setWhatsThis(QtGui.QApplication.translate("MainWindow", "The Description is optional and not needed for the calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Predecessor(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "EST", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "LST", None, QtGui.QApplication.UnicodeUTF8))
        self.loadESTButton.setText(QtGui.QApplication.translate("MainWindow", "Load EST", None, QtGui.QApplication.UnicodeUTF8))
        self.loadLSTButton.setText(QtGui.QApplication.translate("MainWindow", "Load LST", None, QtGui.QApplication.UnicodeUTF8))
        self.efficiencyButton.setText(QtGui.QApplication.translate("MainWindow", "Efficiency", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile_Open.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHere.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuit.setTitle(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_2.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))





if __name__ == '__main__': main()