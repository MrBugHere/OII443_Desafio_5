import pandas as pd
import pickle

class node:
    def __init__(self, data, padre):
        self.data = data
        self.no_visits = 1
        self.prob = 0.0
        self.childs = {}
        self. padre = padre
        
    def actCant(self):
        self.no_visits = self.no_visits + 1
    
    def actProb(self,cant):
        
        self.prob = self.no_visits/cant

    

class tree:
    def __init__(self):
        self.root = node(None,None)

    
 
    def insert(self,string):

        parent = self.root
        for word in string.split():
            if word not in  parent.childs:
                parent.childs[word] = node(word,parent)
                self.actualizarHijos(parent)
            else:
                parent.childs[word].actCant()
                self.actualizarHijos(parent)
            
            parent = parent.childs[word]
    
    def actualizarHijos(self,parent):
        cant = 0
        for hijo in parent.childs.values():
            cant = cant + hijo.no_visits
        
        for hijo in parent.childs.values():
            hijo.actProb(cant)


    def imprimir(self):
        print(self.root.childs['y'].prob)


             



def main():
    arbol = tree()
    datos = pd.read_csv('data_set.csv',header = 0)
    
    for string in datos['transcript']:
        arbol.insert(string)
    arbol.imprimir()
    

main()