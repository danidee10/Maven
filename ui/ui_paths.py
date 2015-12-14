from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 717)
        MainWindow.setMinimumSize(QtCore.QSize(995, 695))
        MainWindow.setMaximumSize(QtCore.QSize(995, 695))
        MainWindow.setStyleSheet("background-color: rgb(63, 63, 63); color: #ffffff;")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 740, 301))
        self.tableWidget.setMaximumSize(QtCore.QSize(740, 301))
        self.tableWidget.setStyleSheet("background-color: #ffffff; color: #000;")
        self.tableWidget.setAlternatingRowColors(True)
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
        self.resultWidget = QtGui.QFrame(self.centralwidget)
        self.resultWidget.setGeometry(QtCore.QRect(745, 2, 245, 338))
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
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.efficiencyLabel.setFont(font)
        self.efficiencyLabel.setText("")
        self.efficiencyLabel.setObjectName("efficiencyLabel")
        self.criticalPathLabel = QtGui.QLabel(self.resultWidget)
        self.criticalPathLabel.setGeometry(QtCore.QRect(10, 40, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.criticalPathLabel.setFont(font)
        self.criticalPathLabel.setStyleSheet("")
        self.criticalPathLabel.setText("")
        self.criticalPathLabel.setObjectName("criticalPathLabel")
        self.projectDurationLabel = QtGui.QLabel(self.resultWidget)
        self.projectDurationLabel.setGeometry(QtCore.QRect(10, 120, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.projectDurationLabel.setFont(font)
        self.projectDurationLabel.setStyleSheet("")
        self.projectDurationLabel.setText("")
        self.projectDurationLabel.setObjectName("projectDurationLabel")
        self.efficiencyTitle = QtGui.QLabel(self.resultWidget)
        self.efficiencyTitle.setGeometry(QtCore.QRect(10, 170, 221, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.efficiencyTitle.setFont(font)
        self.efficiencyTitle.setStyleSheet("font-family: \'Ubuntu\'; font-weight: bold;")
        self.efficiencyTitle.setText("")
        self.efficiencyTitle.setObjectName("efficiencyTitle")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 343, 991, 351))
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.networkDiagram = QtGui.QLabel(self.scrollArea)
        self.networkDiagram.setGeometry(QtCore.QRect(10, 0, 981, 341))
        self.networkDiagram.setText("")
        self.networkDiagram.setObjectName("networkDiagram")
        self.scrollArea.setWidget(self.networkDiagram)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 39))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 3, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calculateButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setUnderline(False)
        font.setBold(False)
        self.calculateButton.setFont(font)
        self.calculateButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.calculateButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(85, 170, 0); \n"
"color: #ffffff; \n"
"border: 1px solid rgb(85, 170, 0); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.calculateButton.setObjectName("calculateButton")
        self.horizontalLayout.addWidget(self.calculateButton)
        self.addRowButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.addRowButton.setFont(font)
        self.addRowButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.addRowButton.setStyleSheet("QPushButton {\n"
"color: #ffffff;\n"
"background-color: rgb(85, 170, 0); \n"
"border: 1px solid rgb(85, 170, 0); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}\n"
"")
        self.addRowButton.setObjectName("addRowButton")
        self.horizontalLayout.addWidget(self.addRowButton)
        self.delRowButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.delRowButton.setFont(font)
        self.delRowButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.delRowButton.setStyleSheet("QPushButton{\n"
"color: #ffffff; \n"
"background-color:  \n"
"tomato; \n"
"border: 1px solid tomato; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.delRowButton.setObjectName("delRowButton")
        self.horizontalLayout.addWidget(self.delRowButton)
        self.viewResourceButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.viewResourceButton.setFont(font)
        self.viewResourceButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(85, 170, 0); \n"
"color: #ffffff; \n"
"border: 1px solid rgb(85, 170, 0); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.viewResourceButton.setObjectName("viewResourceButton")
        self.horizontalLayout.addWidget(self.viewResourceButton)
        self.clearButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.clearButton.setFont(font)
        self.clearButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.clearButton.setStyleSheet("QPushButton{\n"
"color: #ffffff; \n"
"background-color:  tomato; \n"
"border: 1px solid tomato; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 21))
        self.menubar.setStyleSheet("background: none; color: black;")
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Maven", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Id", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setWhatsThis(QtGui.QApplication.translate("MainWindow", "The Description is optional and not needed for the calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Predecessor(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "EST", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "LST", None, QtGui.QApplication.UnicodeUTF8))
        self.calculateButton.setText(QtGui.QApplication.translate("MainWindow", "calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.addRowButton.setText(QtGui.QApplication.translate("MainWindow", "add row", None, QtGui.QApplication.UnicodeUTF8))
        self.delRowButton.setText(QtGui.QApplication.translate("MainWindow", "delete row", None, QtGui.QApplication.UnicodeUTF8))
        self.viewResourceButton.setText(QtGui.QApplication.translate("MainWindow", "view resource loading", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))

