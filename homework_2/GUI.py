# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 570)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #fff")

        self.pallet = QtWidgets.QLabel(self.centralwidget)
        self.pallet.setGeometry(QtCore.QRect(10, 20, 386, 500))
        self.pallet.setText("")
        self.pallet.setObjectName("pallet")
        self.pallet.setStyleSheet('''
                                                     background-color: #afc3de;
                                                     border-style: outset;
                                                     border-color: #afc3de;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                     ''')

        self.heading_label = QtWidgets.QLabel(self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(35, 50, 340, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(16.5)
        self.heading_label.setFont(font)
        self.heading_label.setObjectName("heading_label")
        self.heading_label.setStyleSheet("background-color: #afc3de")


        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(95, 450, 201, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.calculate_button.setFont(font)
        self.calculate_button.setObjectName("calculate_button")
        # self.calculate_button.setStyleSheet('''
        #                                 background-color: #F6ED9A;
        #                                 border-color: #000;
        #                                 border-style: outset;
        #                                 border-width: 2px;
        #                                 border-radius: 5px;
        # ''')

        self.label_D = QtWidgets.QLabel(self.centralwidget)
        self.label_D.setGeometry(QtCore.QRect(30, 120, 181, 16))
        self.label_D.setObjectName("label_D")
        self.label_D.setStyleSheet("background-color: #afc3de")

        self.label_N = QtWidgets.QLabel(self.centralwidget)
        self.label_N.setGeometry(QtCore.QRect(30, 160, 211, 16))
        self.label_N.setObjectName("label_N")
        self.label_N.setStyleSheet("background-color: #afc3de")

        self.label_dt = QtWidgets.QLabel(self.centralwidget)
        self.label_dt.setGeometry(QtCore.QRect(30, 200, 141, 16))
        self.label_dt.setObjectName("label_dt")
        self.label_dt.setStyleSheet("background-color: #afc3de")

        self.label_Nt = QtWidgets.QLabel(self.centralwidget)
        self.label_Nt.setGeometry(QtCore.QRect(30, 240, 231, 16))
        self.label_Nt.setObjectName("label_Nt")
        self.label_Nt.setStyleSheet("background-color: #afc3de")

        self.label_U0 = QtWidgets.QLabel(self.centralwidget)
        self.label_U0.setGeometry(QtCore.QRect(30, 280, 231, 16))
        self.label_U0.setObjectName("label_U0")
        self.label_U0.setStyleSheet("background-color: #afc3de")

        self.label_F_u_t = QtWidgets.QLabel(self.centralwidget)
        self.label_F_u_t.setGeometry(QtCore.QRect(30, 320, 231, 16))
        self.label_F_u_t.setObjectName("label_F_u_t")
        self.label_F_u_t.setStyleSheet("background-color: #afc3de")

        self.label_S = QtWidgets.QLabel(self.centralwidget)
        self.label_S.setGeometry(QtCore.QRect(30, 360, 231, 16))
        self.label_S.setObjectName("label_S")
        self.label_S.setStyleSheet("background-color: #afc3de")

        self.gt_D = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_D.setGeometry(QtCore.QRect(255, 113, 126, 31))
        self.gt_D.setObjectName("gt_D")
        self.gt_D.setStyleSheet("background-color: #f7fafc")

        self.gt_N = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_N.setGeometry(QtCore.QRect(255, 153, 126, 31))
        self.gt_N.setObjectName("gt_N")
        self.gt_N.setStyleSheet("background-color: #f7fafc")

        self.gt_dt = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_dt.setGeometry(QtCore.QRect(255, 193, 126, 31))
        self.gt_dt.setObjectName("gt_dt")
        self.gt_dt.setStyleSheet("background-color: #f7fafc")

        self.gt_Nt = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_Nt.setGeometry(QtCore.QRect(255, 233, 126, 31))
        self.gt_Nt.setObjectName("gt_Nt")
        self.gt_Nt.setStyleSheet("background-color: #f7fafc")

        self.gt_U0 = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_U0.setGeometry(QtCore.QRect(255, 273, 126, 31))
        self.gt_U0.setObjectName("gt_U0")
        self.gt_U0.setStyleSheet("background-color: #f7fafc")

        self.gt_F_u_t = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_F_u_t.setGeometry(QtCore.QRect(255, 313, 126, 31))
        self.gt_F_u_t.setObjectName("gt_F_u_t")
        self.gt_F_u_t.setStyleSheet("background-color: #f7fafc")

        self.gt_S = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_S.setGeometry(QtCore.QRect(255, 353, 126, 31))
        self.gt_S.setObjectName("gt_S")
        self.gt_S.setStyleSheet("background-color: #f7fafc")

        self.rB_heat_map = QtWidgets.QRadioButton(self.centralwidget)
        self.rB_heat_map.setGeometry(QtCore.QRect(38, 405, 131, 20))
        self.rB_heat_map.setObjectName("rB_heat_map")
        self.rB_heat_map.setStyleSheet("background-color: #afc3de")

        self.rB_animate_wave = QtWidgets.QRadioButton(self.centralwidget)
        self.rB_animate_wave.setGeometry(QtCore.QRect(172, 405, 191, 20))
        self.rB_animate_wave.setObjectName("rB_animate_wave")
        self.rB_animate_wave.setStyleSheet("background-color: #afc3de")

        self.surface_output = QtWidgets.QLabel(self.centralwidget)
        self.surface_output.setGeometry(QtCore.QRect(435, 100, 391, 301))
        self.surface_output.setText("")
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(16)
        self.surface_output.setFont(font)
        self.surface_output.setObjectName("surface_output")
        self.surface_output.setWordWrap(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home Assignment 2"))
        self.heading_label.setText(_translate("MainWindow", "<b>Решение уравнения теплопроводности</b>"))
        self.calculate_button.setText(_translate("MainWindow", "Посчитать"))
        self.label_D.setText(_translate("MainWindow", "D - коэффициент диффузии"))
        self.label_N.setText(_translate("MainWindow", "N - количество узлов сетки по X"))
        self.label_dt.setText(_translate("MainWindow", "dt - шаг по времени"))
        self.label_Nt.setText(_translate("MainWindow", "Nt - количество шагов по времени"))
        self.label_U0.setText(_translate("MainWindow", "U0 - начальное условие"))
        self.label_F_u_t.setText(_translate("MainWindow", "F(u(x,t), t) - воздействие"))
        self.label_S.setText(_translate("MainWindow", "S - количество итераций"))
        self.rB_heat_map.setText(_translate("MainWindow", "Тепловая карта"))
        self.rB_animate_wave.setText(_translate("MainWindow", "Анимация профиля волны"))

        self.gt_D.setText(_translate("MainWindow", "0.01"))
        self.gt_N.setText(_translate("MainWindow", "500"))
        self.gt_dt.setText(_translate("MainWindow", "0.1"))
        self.gt_Nt.setText(_translate("MainWindow", "1000"))
        self.gt_U0.setText(_translate("MainWindow", "np.sin(3*x)"))
        self.gt_F_u_t.setText(_translate("MainWindow", "np.sin(0.1*u+t)"))
        self.gt_S.setText(_translate("MainWindow", "5"))

        self.surface_output.setText(_translate("MainWindow", "Для решения уравнения теплопроводности, "
                                                             "пожалуйста, "
                                                             "введите параметры в панели слева, "
                                                             "выберите тип графического отображения "
                                                             "и нажмите на кнопку \"Посчитать\""))


