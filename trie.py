class node:
    def _init_(self, data='', no_visits=1, prob=0., father=None, childs=[]):
        self.data = data
        self.no_visits = no_visits
        self.prob = prob
        self.childs = childs
        self.father = father

    def update_prob(self, cant_visitas_hmnos):
        self.prob = self.no_visits / cant_visitas_hmnos

    def insert_child(self, child):
        self.childs.append(child)

class tree:
    def _init_(self, root=node()):
        self.root = root

    def update_tree(self, node):
        if node.father is None:
            pass

        cant_visitas = 0
        for child in node.father.childs:
            cant_visitas += child.no_visits
        node.update_prob(cant_visitas)

        self.update_tree(node.father)
        
