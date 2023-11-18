from .vetor_ordenado import VetorOrdenado
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Agente:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        #
        #self.objetivo = self.ambiente.get_objective()
        self.encontrato = False
        self.percurso = []
        self.n_vertice_agente = 2
        self.set_agent_in_space(self.ambiente.vertices[self.n_vertice_agente])
        
    def escanear_ambiente(self):
        objetivos = VetorOrdenado(capacidade=10)
        agente = [i for i in self.ambiente.vertices if i.elemento=='A'][0]
        for i in self.ambiente.vertices:
            i.visitado = False
            if i.elemento == 'X':
                i.set_distance(objective= agente)
                objetivos.inserir(i)
        return objetivos
    def func_n_vertice_agente(self):
        agente_vertice = [i for i in range(0, len(self.ambiente.vertices)) if self.ambiente.vertices[i].elemento == 'A']
        return agente_vertice[0]
        
    def clean(self):
        while True:
            self.objetivo = self.escanear_ambiente().valores[0]
            if self.objetivo != None:
                self.ambiente.set_objective(self.objetivo)
                self.busca_gulosa(atual=self.ambiente.vertices[self.func_n_vertice_agente()])
                self.executar_percurso()
            else:
                break

        
            
    def set_agent_in_space(self, grafo_object):
        grafo_object.set_element(new_element="A")
        
    def busca_gulosa(self, atual):
        #print('------')
        #print(f'Atual: ({atual.x_pos},{atual.y_pos})')
        atual.visitado = True
        self.percurso.append(atual)
        if atual == self.objetivo:
          self.encontrado = True
          return
        else:
          vetor_ordenado = VetorOrdenado(capacidade= len(atual.adjacentes))
          for adjacente in atual.adjacentes:
            vetor_ordenado.inserir(adjacente.vertice)
          self.busca_gulosa(vetor_ordenado.valores[0])

    def walk(self, vertice_atual, vertice_novo):
        vertice_atual.set_element(new_element=" ")
        vertice_novo.set_element(new_element="A")
      
    def executar_percurso(self):
        for i in range(1, len(self.percurso)):
            self.ambiente.print_space()
            time.sleep(0.1)
            clear_screen()
            self.walk(vertice_atual=self.percurso[i-1], vertice_novo=self.percurso[i])
        self.percurso = []
        
      