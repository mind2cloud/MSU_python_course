from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 555)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #fff")

        self.pallet = QtWidgets.QLabel(self.centralwidget)
        self.pallet.setGeometry(QtCore.QRect(10, 20, 311, 471))
        self.pallet.setText("")
        self.pallet.setObjectName("pallet")
        self.pallet.setStyleSheet('''
                                                             background-color: #b4b7db;
                                                             border-style: outset;
                                                             border-color: #b4b7db;
                                                             border-width: 2px;
                                                             border-radius: 10px;
                             ''')

        self.heading_label = QtWidgets.QLabel(self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(85, 60, 171, 41))
        font = QtGui.QFont()
        font.setFamily(".Arial")
        font.setPointSize(22)
        self.heading_label.setFont(font)
        self.heading_label.setObjectName("heading_label")
        self.heading_label.setStyleSheet("background-color: #b4b7db")

        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(62, 370, 201, 51))
        font = QtGui.QFont()
        font.setFamily(".Arial")
        font.setPointSize(24)
        self.calculate_button.setFont(font)
        self.calculate_button.setObjectName("calculate_button")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 170, 144, 32))
        self.pushButton.setObjectName("pushButton")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 250, 144, 26))
        self.comboBox.setObjectName("comboBox")

        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(380, 20, 570, 261))
        self.output.setObjectName("output")

        self.kevin_image_label = QtWidgets.QLabel(self.centralwidget)
        self.kevin_image_label.setGeometry(QtCore.QRect(380, 220, 570, 261))
        self.kevin_image_label.setObjectName("kevin_image_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bacon's Number"))
        self.heading_label.setText(_translate("MainWindow", "Число Бейкона"))
        self.calculate_button.setText(_translate("MainWindow", "Посчитать"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить файл"))
        self.output.setText(_translate("MainWindow", ""))
        self.comboBox.hide()
        self.comboBox.addItems(["", "Kevin Bacon", "Johnny Depp", "James McAvoy", "Angelina Joli", "Val Kilmer",
                                "Robert D. Junior", "Scarlett Johansson", "Joseph Gordon-Levitt", "Natalie Portman",
                                "Benedict Cumberbatch"])
