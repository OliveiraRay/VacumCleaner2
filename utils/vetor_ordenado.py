import numpy as np

class VetorOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(capacidade, dtype=object)

  def imprimeVetor(self):
    if self.ultima_posicao == -1:
      print('Vetor Vazio!')
    else:
      for i in range(self.ultima_posicao+1):
        print(f"{self.valores[i].x_pos} {self.valores[i].y_pos} {round(self.valores[i].distance, 3)}")
  def inserir(self, vertice):
    if self.ultima_posicao == self.capacidade -1:
      print('Capacidade Maxima Atingida')
      return

    posicao =0
    for i in range(self.ultima_posicao +1):
      posicao=i
      if self.valores[i].distance > vertice.distance:
        break
      if i == self.ultima_posicao:
        posicao = i+1

    x = self.ultima_posicao
    while x>=posicao:
      self.valores[x+1] = self.valores[x]
      x-=1
    self.valores[posicao] = vertice
    self.ultima_posicao+=1