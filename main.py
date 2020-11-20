import pandas as pd
import pickle as pc
from trie import tree


if __name__ == "__main__":
    arbol = tree()
    datos = pd.read_csv('data_set.csv',header = 0)

    i = 0
    print(datos['transcript'])
    for string in datos['transcript']:
        arbol.insert(string)
        print(i)
        i+=1

    """for i in range(int(len(datos['transcript'])*.1)):
        arbol.insert(datos['transcript'][i])
        print(i)"""

    #arbol.load_tree("save_state_tree.p")
    arbol.imprimir()

    print(arbol.recommend("y", 4))
    print()
    print(arbol.recommend("come tu", 2))

    #arbol.save_tree()
