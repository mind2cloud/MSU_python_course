import matplotlib.pyplot as plt
import networkx as nx
import json
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from GUI import Ui_GUI

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_GUI()
        self.ui.setupUi(self)
        self.current_text = None
        self.ui.pushButton.clicked.connect(self.open_file_picker)
        self.ui.comboBox.currentTextChanged.connect(self.on_combobox)
        self.ui.calculate_button.clicked.connect(self.output_label_result)


    def on_combobox(self, text):
        self.current_text = text
        print(self.current_text)


    def open_file_picker(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Выбрать файл: (МГУ ван лав)", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.ui.comboBox.show()
            # print(fileName)

    def output_label_result(self):
        actor_ = self.current_text
        with open("data_need.json", "r") as read_file:
            data = json.load(read_file)
            graph = nx.Graph()
            for actor in data:
                graph.add_edge(actor['names'][0], actor['names'][1], films=actor['films'])

            bacon_number = nx.dijkstra_path(graph, actor_, 'Kevin Bacon')
            length = len(bacon_number) - 1

            actor_paths = []
            invador = ''
            for i in range(0, length):
                actor_paths.append(graph.get_edge_data(bacon_number[i], bacon_number[i + 1]))
                for names, films in actor_paths[i].items():
                    invador += str(bacon_number[i]) + " was in " + str(films) + " with " + str(bacon_number[i + 1]) + "\n"
                    print(invador)
            header = "Path from " + str(actor_) + " to Kevin Bacon:" + "\n"
            text = str(header) + invador + str(actor_) + "'s Kevin Bacon number is " + str(length) + ".\n"
            self.ui.output.setText(text)
            pixmap = QPixmap("kevin.jpg")
            self.ui.kevin_image_label.setPixmap(pixmap)

    def get_films(self, actor_1, actor_2):
        with open("data_need.json", "r") as read_file:
            data = json.load(read_file)
            for actor in data:
                if (actor_1 in actor['names'][0]) and (actor_2 in actor['names'][1]) or (actor_1 in actor['names'][1]) and (actor_2 in actor['names'][0]):
                    return actor['films']


# def main():
    # graph = nx.Graph()
    # actors = []
    # G = nx.Graph()
    # a = Baicon_number("A", "A", 'a')
    # b = Baicon_number("B", "B", 'b')
    # c = Baicon_number("B", "B", 'b')
    # d = Baicon_number("D", "D", 'd')
    #
    # G.add_node(a)
    # G.add_node(b)
    # G.add_node(c)
    # G.add_node(d)
    #
    # G.add_edges_from([(a, b), (b, c), (b,d)])
    # path = nx.dijkstra_path(G, a, d)
    # print(len(path) - 1)
    #
    # # nx.draw(G)
    # nx.draw(G, pos=nx.spring_layout(G))  # use spring layout
    #
    # plt.show()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

# if __name__ == "__main__":
#     main()
