## OII443_Desafio_5

Uno de los pasatiempos de Amanda es la escritura, pasar horas frente a un computador o con un cuaderno escribiendo historias de todo tipo siempre la relaja. Con la llegada de la pandemia al país, ella noto que dedica más horas de su semana a redactar sus novelas. Además, noto que existen palabras y frases que usa comúnmente, por lo que necesita ayuda para identificar sus muletillas al escribir para corregirlas según sea la necesidad.

## Objetivos

Procesar la información otorgada para mejor trabajo posterior.
Utilizar los conocimientos del módulo para la solución de un problema.

### Descripción

Para ejecutar el codigo hay que tener instalado python 3, y ejecutar el archivo main.py. Para procesar la informacion se empleara la estructura trie, la cual utilizara las clases:

```python
class node:
    def __init__(self, data, padre):
        self.data = data
        self.no_visits = 1
        self.prob = 0.0
        self.childs = {}
        self.padre = padre
``` 
```python
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
``` 
Para crear el arbol se utiliza la funcion "insert" y "actualizarHijos", luego una ves poblado con todos los datos del archivo "data_set.csv" se guarda utilizando la funcion "save_tree". Finalmente con la funcion "recommend" se recomienda las palabras con una mayor probabilidad de quesean util para seguir la oracion.

