def alocar_professores(Grafo, nLaboratorios):
    nTurmasT = len([n for n, d in Grafo.nodes(data=True) if d['bipartite'] == 1])
    nProfessores = int(input("Digite o número de professores: "))

    professores = [f"Prof{i+1}" for i in range(nProfessores)]
    for prof in professores:
        Grafo.add_node(prof, bipartite=2)

    nHorarios = (nTurmasT // nProfessores) + 1 if nProfessores <= nLaboratorios else (nTurmasT // nLaboratorios) + 1

    turmas = [n for n, d in Grafo.nodes(data=True) if d['bipartite'] == 1]
    for i, turma in enumerate(turmas):
        Grafo.add_edge(professores[i % nProfessores], turma)

    return nHorarios

def alocar_horarios(Grafo, nHorariosT):
    nDias = 3
    nHorarios = 3
    turmas = [n for n, d in Grafo.nodes(data=True) if d['bipartite'] == 1]
    turma_index = 0

    for k in range(2):
        for i in range(nDias):
            if i == 2:
                for j in range(1, 3):
                    node = f"D{i+1}H{j}"
                    Grafo.add_node(node, bipartite=3)
                    if turma_index < len(turmas):
                        t = turmas[turma_index]
                        prof = [n for n in Grafo.neighbors(t) if Grafo.nodes[n]['bipartite'] == 2][0]
                        Grafo.add_edge(node, t)
                        Grafo.add_edge(node, prof)
                        turma_index += 1
            else:
                for j in range(nHorarios):
                    for offset in [0, 2]:
                        node = f"D{i+1+offset}H{j+1}"
                        Grafo.add_node(node, bipartite=3)
                        if turma_index < len(turmas):
                            t = turmas[turma_index]
                            prof = [n for n in Grafo.neighbors(t) if Grafo.nodes[n]['bipartite'] == 2][0]
                            Grafo.add_edge(node, t)
                            Grafo.add_edge(node, prof)
                            turma_index += 1
