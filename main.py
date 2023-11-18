from utils.agente import *
from utils.espaco import *
from utils.vetor_ordenado import *
    
def run():
    espaco = Espaco(shape_x=20, shape_y=20)
    agente = Agente(ambiente=espaco)
    agente.clean()
    
if __name__ == "__main__":
    run()