# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\level.ui'
#
# Created: Sun Aug 23 17:16:49 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 695)
        MainWindow.setMinimumSize(QtCore.QSize(995, 695))
        MainWindow.setMaximumSize(QtCore.QSize(995, 695))
        MainWindow.setStyleSheet("background-color: rgb(63, 63, 63); color: #ffffff;")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(750, 10, 111, 211))
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
        self.addRowButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.addRowButton.setStyleSheet("QPushButton {\n"
"color: #ffffff;\n"
"background-color: rgb(85, 170, 0); \n"
"border: 1px solid rgb(85, 170, 0); \n"
"padding: 5px; \n"
"height: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}\n"
"")
        self.addRowButton.setObjectName("addRowButton")
        self.verticalLayout.addWidget(self.addRowButton)
        self.calculateButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.calculateButton.setFont(font)
        self.calculateButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.calculateButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(85, 170, 0); \n"
"color: #ffffff; \n"
"border: 1px solid rgb(85, 170, 0); \n"
"padding: 5px; \n"
"height: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.calculateButton.setObjectName("calculateButton")
        self.verticalLayout.addWidget(self.calculateButton)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 740, 301))
        self.tableWidget.setMaximumSize(QtCore.QSize(740, 301))
        self.tableWidget.setStyleSheet("background-color: #ffffff; color: #666;")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
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
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(870, 10, 117, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.delRowButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.delRowButton.setFont(font)
        self.delRowButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.delRowButton.setStyleSheet("QPushButton{\n"
"color: #ffffff; \n"
"background-color:  \n"
"tomato; \n"
"border: 1px solid tomato; \n"
"padding: 5px; \n"
"height: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.delRowButton.setObjectName("delRowButton")
        self.verticalLayout_2.addWidget(self.delRowButton)
        self.clearButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.clearButton.setFont(font)
        self.clearButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.clearButton.setStyleSheet("QPushButton{\n"
"color: #ffffff; \n"
"background-color:  \n"
"tomato; \n"
"border: 1px solid tomato; \n"
"padding: 5px; \n"
"height: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout_2.addWidget(self.clearButton)
        self.resultWidget = QtGui.QFrame(self.centralwidget)
        self.resultWidget.setGeometry(QtCore.QRect(750, 320, 241, 351))
        self.resultWidget.setStyleSheet("QFrame{\n"
"border: 1px solid #ffffff;\n"
"}\n"
"\n"
"QLabel{\n"
"border:none;\n"
"}\n"
"\n"
"QMenu{\n"
"background-color: red;\n"
"}")
        self.resultWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.resultWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.resultWidget.setObjectName("resultWidget")
        self.efficiencyLabel = QtGui.QLabel(self.resultWidget)
        self.efficiencyLabel.setGeometry(QtCore.QRect(10, 190, 221, 17))
        font = QtGui.QFont()
        font.setFamily("comic sans MS")
        font.setWeight(75)
        font.setBold(True)
        self.efficiencyLabel.setFont(font)
        self.efficiencyLabel.setStyleSheet("font-family: \'comic sans MS\'; font-weight: bold; font-size: 14px;")
        self.efficiencyLabel.setText("")
        self.efficiencyLabel.setObjectName("efficiencyLabel")
        self.criticalPathLabel = QtGui.QLabel(self.resultWidget)
        self.criticalPathLabel.setGeometry(QtCore.QRect(10, 40, 211, 51))
        font = QtGui.QFont()
        font.setFamily("comic sans MS")
        font.setWeight(75)
        font.setBold(True)
        self.criticalPathLabel.setFont(font)
        self.criticalPathLabel.setStyleSheet("font-family: \'comic sans MS\'; font-weight: bold; font-size: 14px;")
        self.criticalPathLabel.setText("")
        self.criticalPathLabel.setObjectName("criticalPathLabel")
        self.projectDurationLabel = QtGui.QLabel(self.resultWidget)
        self.projectDurationLabel.setGeometry(QtCore.QRect(10, 120, 221, 41))
        font = QtGui.QFont()
        font.setFamily("comic sans MS")
        font.setWeight(75)
        font.setBold(True)
        self.projectDurationLabel.setFont(font)
        self.projectDurationLabel.setStyleSheet("font-family: \'comic sans MS\'; font-weight: bold; font-size: 14px;")
        self.projectDurationLabel.setText("")
        self.projectDurationLabel.setObjectName("projectDurationLabel")
        self.efficiencyTitle = QtGui.QLabel(self.resultWidget)
        self.efficiencyTitle.setGeometry(QtCore.QRect(10, 175, 221, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.efficiencyTitle.setFont(font)
        self.efficiencyTitle.setStyleSheet("font-family: \'Ubuntu\'; font-weight: bold; font-size: 14px;")
        self.efficiencyTitle.setText("")
        self.efficiencyTitle.setObjectName("efficiencyTitle")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 320, 741, 351))
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.networkDiagram = QtGui.QLabel(self.scrollArea)
        self.networkDiagram.setGeometry(QtCore.QRect(10, 0, 731, 341))
        self.networkDiagram.setText("")
        self.networkDiagram.setObjectName("networkDiagram")
        self.scrollArea.setWidget(self.networkDiagram)
        self.viewResourceButton = QtGui.QPushButton(self.centralwidget)
        self.viewResourceButton.setGeometry(QtCore.QRect(750, 220, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.viewResourceButton.setFont(font)
        self.viewResourceButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(85, 170, 0); \n"
"color: #ffffff; \n"
"border: 1px solid rgb(85, 170, 0); \n"
"padding: 5px; \n"
"height: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.viewResourceButton.setObjectName("viewResourceButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 21))
        self.menubar.setStyleSheet("background: none; color: black;")
        self.menubar.setObjectName("menubar")
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
        self.menubar.addAction(self.menuHere.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.addRowButton, self.tableWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.addRowButton.setText(QtGui.QApplication.translate("MainWindow", "Add Row", None, QtGui.QApplication.UnicodeUTF8))
        self.calculateButton.setText(QtGui.QApplication.translate("MainWindow", "Calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Id", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setWhatsThis(QtGui.QApplication.translate("MainWindow", "The Description is optional and not needed for the calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Predecessor(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "EST", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "LST", None, QtGui.QApplication.UnicodeUTF8))
        self.delRowButton.setText(QtGui.QApplication.translate("MainWindow", "Del Row", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.viewResourceButton.setText(QtGui.QApplication.translate("MainWindow", "View resource loading", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHere.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuit.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_2.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))

