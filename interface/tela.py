import os
from core.grafo import criar_grafo_disc_lab
from core.visualizacao import visualizar_grafo_interativo

def iniciar_sistema():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sistema de Gerenciamento de Laboratórios")
    grafo = criar_grafo_disc_lab()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Turma - Professor - Laboratório - Dia e Horário")
    
    for node in grafo.nodes(data=True):
        if node[1].get('bipartite') == 1:
            professor = [n for n in grafo.neighbors(node[0]) if grafo.nodes[n].get('bipartite') == 2]
            lab = [n for n in grafo.neighbors(node[0]) if grafo.nodes[n].get('bipartite') == 0]
            DH = [n for n in grafo.neighbors(node[0]) if grafo.nodes[n].get('bipartite') == 3]
            print(f"{node[0]}  - {', '.join(professor)} - {', '.join(lab)} - {', '.join(DH)}")
    
    plt_obj = visualizar_grafo_interativo(grafo)
    plt_obj.show()



