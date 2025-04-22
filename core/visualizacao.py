import os
import networkx as nx                                                                       # type: ignore
import matplotlib.pyplot as plt                                                             # type: ignore

def visualizar_grafo_interativo(grafo):
    plt.figure(figsize=(12, 10))
    laboratorios = [node for node, data in grafo.nodes(data=True) if data.get('bipartite') == 0]
    turmas = [node for node, data in grafo.nodes(data=True) if data.get('bipartite') == 1]
    professores = [node for node, data in grafo.nodes(data=True) if data.get('bipartite') == 2]
    horarios = [node for node, data in grafo.nodes(data=True) if data.get('bipartite') == 3]
    pos = {}
    for i, lab in enumerate(laboratorios):
        pos[lab] = (i * 2, 3)
    for i, turma in enumerate(turmas):
        pos[turma] = (i * 2, 2)
    for i, prof in enumerate(professores):
        pos[prof] = (i * 3, 1)
    for i, horario in enumerate(horarios):
        pos[horario] = (i * 1.5, 0)
    node_colors = {}
    for node in laboratorios:
        node_colors[node] = 'lightblue'
    for node in turmas:
        node_colors[node] = 'lightgreen'
    for node in professores:
        node_colors[node] = 'salmon'
    for node in horarios:
        node_colors[node] = 'yellow'
    all_edges = list(grafo.edges())
    edge_collection = nx.draw_networkx_edges(grafo, pos, edgelist=all_edges, 
                                           edge_color='#555555', width=1.0, alpha=0.5)
    node_collection = nx.draw_networkx_nodes(grafo, pos, 
                                           node_color=[node_colors[node] for node in grafo.nodes()],
                                           node_size=700)
    nx.draw_networkx_labels(grafo, pos, font_size=10, font_weight='bold')
    lab_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', 
                          markersize=10, label='Laboratórios')
    turma_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', 
                            markersize=10, label='Turmas')
    prof_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='salmon', 
                           markersize=10, label='Professores')
    horario_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', 
                              markersize=10, label='Horários')
    plt.legend(handles=[lab_patch, turma_patch, prof_patch, horario_patch])
    plt.title("Alocação de Laboratórios, Professores e Horários para Turmas\n(Clique em um nó para destacar suas conexões)")
    plt.axis('off')
    last_clicked_node = [None]
    highlighted_edge_collection = [None]
    def on_click(event):
        if event.inaxes is not None:
            cont, ind = node_collection.contains(event)
            if cont:
                node_idx = ind["ind"][0]
                clicked_node = list(grafo.nodes())[node_idx]
                edge_collection.set_color('#555555')
                edge_collection.set_linewidth(1.0)
                edge_collection.set_alpha(0.5)
                if highlighted_edge_collection[0] is not None:
                    highlighted_edge_collection[0].remove()
                    highlighted_edge_collection[0] = None
                if clicked_node == last_clicked_node[0]:
                    last_clicked_node[0] = None
                    plt.title("Alocação de Laboratórios, Professores e Horários para Turmas\n(Clique em um nó para destacar suas conexões)")
                    plt.draw()
                    return
                last_clicked_node[0] = clicked_node
                highlighted_edges = []
                for u, v in grafo.edges():
                    if u == clicked_node or v == clicked_node:
                        highlighted_edges.append((u, v))
                if highlighted_edges:
                    highlighted_edge_collection[0] = nx.draw_networkx_edges(
                        grafo, pos, edgelist=highlighted_edges, 
                        edge_color='#CC0000',  
                        width=2.5, 
                        alpha=1.0
                    )
                node_info = f"Nó: {clicked_node}"
                if clicked_node in turmas:
                    professor = [n for n in grafo.neighbors(clicked_node) if grafo.nodes[n].get('bipartite') == 2]
                    lab = [n for n in grafo.neighbors(clicked_node) if grafo.nodes[n].get('bipartite') == 0]
                    DH = [n for n in grafo.neighbors(clicked_node) if grafo.nodes[n].get('bipartite') == 3]
                    professorstring = ", ".join(professor) if professor else "Nenhum"
                    labstring = ", ".join(lab) if lab else "Nenhum"
                    DHstring = ", ".join(DH) if DH else "Nenhum"
                    node_info += f"\nProfessor: {professorstring}\nLaboratório: {labstring}\nHorários: {DHstring}"
                plt.title(node_info)
                plt.draw()
    plt.gcf().canvas.mpl_connect('button_press_event', on_click)
    return plt