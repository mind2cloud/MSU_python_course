import networkx as nx
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
import json
import itertools

interface = tk.Tk()
interface.geometry('600x200')
interface.title("Bacon's Number")

downloaded_file = StringVar()
downloaded_file_name = Entry(interface, width=45, font='Times 14', textvariable = downloaded_file)
downloaded_file_name.grid(row=3, column=3, columnspan=2)

class Homework3:
    def __init__(self):
        self.__dataset = {}
        self.__data = []
        self.__Graph = nx.Graph()
        self.__nodes = []

    def setData(self, data):
        self.__clearData()
        self.__data = data
        self.__setDataset()
        self.__setNodes()
        self.__buildGraph()

    def __clearData(self):
        self.__dataset = {}
        self.__data = []
        self.__Graph = nx.Graph()
        self.__nodes = []

    def __setDataset(self):
        for actor in self.__data:
            for film in actor['films']:
                title_plus_year = film['title'] + ' (' + str(film['year']) + ')'
                if title_plus_year in self.__dataset.keys():
                    self.__dataset[title_plus_year].append(actor['name'])
                else:
                    self.__dataset[title_plus_year] = []
                    self.__dataset[title_plus_year].append(actor['name'])

    def __setNodes(self):
        for actor in self.__data:
            self.__nodes.append(actor['name'])

    def __buildGraph(self):
        self.__Graph.add_nodes_from(self.__nodes)

        for value in self.__dataset.values():
            pairsOfVertices = list(itertools.combinations(value, 2))
            if (len(pairsOfVertices) >= 1):
                self.__Graph.add_edges_from(pairsOfVertices)

    def getNodes(self):
        return self.__nodes

    def findBaconNumber(self, actorName):
        pathFromNames = nx.shortest_path(self.__Graph, source=actorName, target='Kevin Bacon')
        text = ''
        baconNumber = len(pathFromNames) - 1

        def getFilm(actor1, actor2):
            for film, names in self.__dataset.items():
                if (actor1 in names) and (actor2 in names):
                    return film

        for i in range(baconNumber):
            actor1 = pathFromNames[i]
            actor2 = pathFromNames[i + 1]
            film = getFilm(actor1, actor2)
            text += actor1 + ' was in ' + film + ' with ' + actor2 + '\n'
        text += pathFromNames[0] + '\'s' + ' Bacon number is ' + str(baconNumber) + '\n'

        return text

Graph = Homework3()

def chosen_file():
    route = askopenfilename()
    downloaded_file.set(route)

def load_data():
    with open(downloaded_file.get(), 'r', encoding='utf-8') as file:
        Graph.setData(json.load(file))
    combo['values'] = Graph.getNodes()
    combo.current(0)

def printBaconNumber(event):
    actor = combo.get()
    result['text'] = Graph.findBaconNumber(actor)

choose_a_file_button = Button(interface, width=20, text = "Choose a file",font='Times 14', command = chosen_file)
choose_a_file_button.grid(row=1, column=3, columnspan=2)

load_button = Button(interface, width=20, text = "Load", font='Times 14', command = load_data)
load_button.grid(row=2, column=3, columnspan=2)

actor_or_actress = Label(interface, text = "Actor/Actress: ", font='Times 14')
actor_or_actress.grid(row=4, column=0, columnspan=1)

result = Label(interface, font='Times 14')
result.grid(row=5, column=1, columnspan=10)

combo = Combobox(interface, width = 45)
combo.grid(row=4, column=1, columnspan=5)
combo.bind("<<ComboboxSelected>>", printBaconNumber)

interface.mainloop()