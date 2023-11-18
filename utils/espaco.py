import itertools
import random as rd

class Vertice:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.elemento= " "
        self.adjacentes = []
        self.distance = None
        self.visitado = False

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        print("X Y")
        for i in self.adjacentes:
            print(f"{i.vertice.x_pos}-{i.vertice.y_pos}")
    def set_element(self, new_element):
      self.elemento= new_element
    def set_distance(self, objective):
      self.distance = (((self.x_pos-objective.x_pos)**2) + (self.y_pos-objective.y_pos)**2)**0.5

class Adjacente:
    def __init__(self, vertice):
        self.vertice = vertice
        self.custo = 1

class Espaco:
    def __init__(self, shape_x, shape_y):
        self.shape_x = shape_x
        self.shape_y = shape_y
        self.vertices = []
    
        self.create_vertices()
        self.create_adjacentes()

        self.gen_dirty()


    def gen_dirty(self):
        nums = [rd.randint(0, len(self.vertices)) for i in range(9)]
        for num in nums:
            self.vertices[num].set_element('X')
            
    def set_objective(self, objetivo):
        objetivo.set_element('X')
        for i in self.vertices:
            i.set_distance(objetivo)
            
    def get_objective(self):
        for i in self.vertices:
            if i.elemento == 'X':
                return i
            
    def create_vertices(self):
        for i in itertools.product(range(self.shape_x), range(self.shape_y)):
            self.vertices.append(Vertice(x_pos=i[0], y_pos=i[1]))
            
    def get_vertice(self, x_pos, y_pos):
        for vertice in self.vertices:
            if vertice.x_pos == x_pos and vertice.y_pos == y_pos:
                return vertice
                
    def create_adjacentes(self):
        for vertice in self.vertices:
            # Em cima
            em_cima = self.get_vertice(x_pos=vertice.x_pos+1, y_pos=vertice.y_pos)
            if em_cima != None:
                vertice.adiciona_adjacente(Adjacente(em_cima))

            # Em baixo
            em_baixo = self.get_vertice(x_pos=vertice.x_pos-1, y_pos=vertice.y_pos)
            if em_baixo != None:
                vertice.adiciona_adjacente(Adjacente(em_baixo))
        
            # Direita
            direita = self.get_vertice(x_pos=vertice.x_pos, y_pos=vertice.y_pos+1)
            if direita != None:
                vertice.adiciona_adjacente(Adjacente(direita))
            # Esquerda
            esquerda = self.get_vertice(x_pos=vertice.x_pos, y_pos=vertice.y_pos-1)
            if esquerda != None:
                vertice.adiciona_adjacente(Adjacente(esquerda))
    def print_space(self):
        state = []
        for i in range(self.shape_x):
            line = [self.get_vertice(x_pos=i, y_pos=j).elemento for j in range(self.shape_y)]
            print(line)