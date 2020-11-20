import pickle as pc


class node:
    def __init__(self, data, padre):
        self.data = data
        self.no_visits = 1
        self.prob = 0.0
        self.childs = {}
        self.padre = padre

    def actCant(self):
        self.no_visits = self.no_visits + 1

    def actProb(self, cant):
        self.prob = self.no_visits / cant


class tree:
    def __init__(self):
        self.root = node(None, None)

    def save_tree(self):
        pc.dump(self.root, open("save_state_tree.p", "wb"))

    def load_tree(self, input):
        self.root = pc.load(open(input, "rb"))

    def insert(self, string):
        parent = self.root
        for word in string.split():
            if word not in parent.childs:
                parent.childs[word] = node(word, parent)
                self.actualizarHijos(parent)
            else:
                parent.childs[word].actCant()
                self.actualizarHijos(parent)

            parent = parent.childs[word]

    def actualizarHijos(self, parent):
        cant = 0
        for hijo in parent.childs.values():
            cant += hijo.no_visits

        for hijo in parent.childs.values():
            hijo.actProb(cant)

    def imprimir(self):
        print(self.root.childs['cuando'].prob)

    def getprobsum(self):
        sum = 0
        for child in self.root.childs.values():
            sum += child.prob
        return sum

    def recommend(self, sentence, k):
        parent = self.root
        words = sentence.split()
        for word in words:
            if word not in parent.childs:
                return "Lo sentimos, la palabra no se encuentra en el diccionario, por lo tanto no posee recomendaciones."
            parent = parent.childs[word]

            if word == words[-1]:
                if not parent.childs:
                    return "Lo sentimos, la palabra se encuentra en el diccionario, pero no posee recomendaciones."
                childsprob = []
                for child in parent.childs.values():
                    childsprob.append((str(child.prob),child.data))
                childsprob.sort(reverse=True)
                if k > len(childsprob):
                    return "\n".join(childsprob)
                else:
                    predictions = ""
                    for i in range(k):
                        predictions = "\n".join([predictions," - ".join([childsprob[i][0],childsprob[i][1]])])
                    return predictions

