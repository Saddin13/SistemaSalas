import networkx as nx
from core.alocacao import alocar_professores, alocar_horarios

def criar_grafo_disc_lab():
    Grafo = nx.Graph()

    nLaboratorios = int(input("Digite o número de laboratórios Disponíveis: "))
    for i in range(nLaboratorios):
        Grafo.add_node(f"Lab{i+1}", bipartite=0)

    nDisciplinas = int(input("Digite o número de disciplinas: "))
    nLabU = 1
    for i in range(nDisciplinas):
        nTurmas = int(input(f"Digite o número de turmas da disciplina {i+1}: "))
        for j in range(nTurmas):
            turma = f"M{i+1}T{j+1}"
            Grafo.add_node(turma, bipartite=1)
            lab = f"Lab{nLabU}"
            Grafo.add_edge(turma, lab)
            nLabU = nLabU + 1 if nLabU < nLaboratorios else 1

    nHorarios = alocar_professores(Grafo, nLaboratorios)
    alocar_horarios(Grafo, nHorarios)

    return Grafo



