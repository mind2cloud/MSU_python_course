# from tkinter import *

# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from GUI import Ui_GUI

import random




class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_GUI()
        self.ui.setupUi(self)
        self.ui.calculate_button.clicked.connect(self.Go)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        #self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QtWidgets.QVBoxLayout()
        #layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)


        #self.MyUI()

    def MyUI(self):

        canvas = Canvas(self, width=3, height=1)
        canvas.move(5, 5)

    def RP(self, u, t):
        print(self.ui.gt_F_u_t.text())
        try:
            return eval(self.ui.gt_F_u_t.text())
        except:
            print("Bad F(u(x,t),t)")
            sys.exit(2)

    def Go(self, eve):
        print('inside Go')
        global  D,N,dt,Nt,s,z
        try:
            D = float(self.ui.gt_D.text())
            print(D)
            N = int(self.ui.gt_N.text())
            print(N)
            dt = float(self.ui.gt_dt.text())
            print(dt)
            Nt = int(self.ui.gt_Nt.text())
            print(Nt)
            s = int(self.ui.gt_S.text())
            print(s)
        except:
            print("Bad input!")
            sys.exit(1)

        z = np.zeros((Nt, N))

        if (N%2 != 0):
                N = N + 1

        l = [0.0]  # , type = "float") #собственные значения
        h = 2 * np.pi / N
        x = np.zeros(N)

        for i in range(0, N):
            x[i] = (i * h)

        func = eval(self.ui.gt_U0.text())
        u0 = func
        z[0] = u0

        # считаем коэффициенты лямбда
        for k in range(int(-N/2), 0):
            if k==-N/2 :
                l.insert (1, 4 * D / h ** 2 * (np.sin (k * h / 4)) ** 2)
            else :
                l.insert(1, 4 * D / h ** 2 * (np.sin (k * h / 4)) ** 2)
                l.append (4 * D / h ** 2 * (np.sin(-k * h / 4)) ** 2)

        l = np.array(l)

        #решение
        for k in range(1, Nt):  # NT - колиичество шагов по времени
            Upast = z[k - 1]  # предыдущий шаг
            U_current = Upast
            for i in range(s):
                Ф1 = self.RP(Upast, (k-1)*dt)
                Ф2 = self.RP(U_current, k * dt)
                HalfArray = (Ф1+Ф2)
                fu = np.fft.fft(HalfArray)
                fuu = np.fft.fft(Upast)
                FurieUcurrent = ((2 - l * dt) * fuu + dt * fu) / (2 + l * dt)
                U_current = np.fft.ifft(FurieUcurrent)
            z[k] = U_current


        if self.ui.rB_heat_map.isChecked():
            print('Heat Map')
            fig = plt.figure()  # пустая фигура
            im = plt.imshow(z.transpose())  # рисует карту
            plt.savefig("image_to_label.png")
            pixmap = QPixmap("image_to_label.png")
            self.ui.surface_output.setPixmap(pixmap)

        elif self.ui.rB_animate_wave.isChecked():
            # root = Tk()
            # root.geometry('600x680+300+200')
            # root.resizable(width=False, height=False)
            # root.title("Решение уравнения теплопроводности")

            fig, ax = plt.subplots()
            # plt.xlim(0, 2*np.pi)
            plt.ylim(z.min(), z.max())
            x = range(0, N)

            line, = ax.plot(x, z[0])

            def init():
                line.set_ydata(np.ma.array(x, mask=True))
                return line,

            def frame(i):
                line.set_ydata(z[i])  # update the data
                return line,

            def output():
                ani = animation.FuncAnimation(fig, frame, np.arange(0, Nt), init_func=init, interval=300 * dt,
                                              blit=True)
                ani.save('gif_to_label.gif', writer='imagemagick')
                # #canvas.draw()
                # ani.show()

            #canvas = FigureCanvasTkAgg(fig, master=root)
            #canvas.get_tk_widget().grid(column=0, row=10, columnspan=4)

            output()
            # canvas = Canvas(self, width=3, height=1)
            # canvas.move(5, 5)
            # ''' plot some random stuff '''
            # # random data
            # data = [random.random() for i in range(10)]
            #
            # # instead of ax.hold(False)
            # self.figure.clear()
            #
            # # create an axis
            # ax = self.figure.add_subplot(111)
            #
            # # discards the old graph
            # # ax.hold(False) # deprecated, see above
            #
            # # plot data
            # ax.plot(data, '*-')
            # # refresh canvas
            # self.canvas.draw()


            print('Animate Wave')
            # ------------------------------------------------------
            # fig, ax = plt.subplots()
            # # plt.xlim(0, 2*np.pi)
            # plt.ylim(z.min(), z.max())
            # x = range(0, N)
            #
            # line, = ax.plot(x, z[0])
            #
            # def init():
            #     line.set_ydata(np.ma.array(x, mask=True))
            #     return line,
            #
            # def frame(i):
            #     line.set_ydata(z[i])  # update the data
            #     return line,
            #
            # def output():
            #     self.figure.clear()
            #     ax = self.ui.figure.add_subplot(111)
            #
            #
            #     ani = animation.FuncAnimation(fig, frame, np.arange(0, Nt), init_func=init, interval=300 * dt, blit=True)
            #     #ani.save('gif_to_label.gif', writer='imagemagick')
            #     # self.fui.surface_output.show()
            #     # canvas = FigureCanvasTkAgg(fig, master=root)
            #     # canvas.get_tk_widget().grid(column=0, row=10, columnspan=4)
            #
            #     self.canvas.draw()

                # root = Tk()
                # root.geometry('600x680+300+200')
                # root.resizable(width=False, height=False)
                # root.title("Решение уравнения теплопроводности")
                # canvas = FigureCanvasTkAgg(fig, master=root)
                # canvas.get_tk_widget().grid(column=0, row=10, columnspan=4)
                # root.mainloop()
        #
        #     canvas = FigureCanvasTkAgg(fig, master=root)
        #     canvas.get_tk_widget().grid(column=0, row=10, columnspan=4)
        #     self.ui.surface_output = canvas
        #
        #     output()
            # ------------------------------------------------------



# class Canvas(FigureCanvas):
#     def __init__(self, parent=None, width=5, height=5, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#
#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
#
#         self.plot()
#
#     def plot(self):
#         z = np.zeros((Nt, N))
#         fig, ax = plt.subplots()
#         # plt.xlim(0, 2*np.pi)
#         plt.ylim(z.min(), z.max())
#         x = range(0, N)
#
#         line, = ax.plot(x, z[0])
#
#         def init():
#             line.set_ydata(np.ma.array(x, mask=True))
#             return line,
#
#         def frame(i):
#             line.set_ydata(z[i])  # update the data
#             return line,
#
#         def output():
#             self.figure.clear()
#             ax = self.ui.figure.add_subplot(111)
#
#
#             ani = animation.FuncAnimation(fig, frame, np.arange(0, Nt), init_func=init, interval=300 * dt, blit=True)
#         x = np.array([50, 30, 40])
#         labels = ["Apples", "Bananas", "Melons"]
#         ax = self.figure.add_subplot(111)
#         ax.pie(x, labels=labels)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()



sys.exit(app.exec())
