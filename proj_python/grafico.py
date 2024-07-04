import matplotlib.pyplot as plt
import networkx as nx


G = nx.DiGraph()


componentes = {
    'Frontend': ('Frontend\n(Desktop, Mobile, Apple Watch)', 'ellipse'),
    'Backend': ('Backend\n(Serviços)', 'ellipse'),
    'IA_ML': ('Inteligência Artificial\nMachine Learning', 'ellipse'),
    'BD_Armazenamento': ('Base de Dados\nArmazenamento', 'ellipse'),
    'Infraestrutura': ('Infraestrutura', 'ellipse'),
    'Seguranca': ('Segurança\nPrivacidade', 'ellipse'),
    'Lançamento': ('Lançamento', 'ellipse')
}


for key, value in componentes.items():
    G.add_node(key, label=value[0], shape=value[1])

# Adiciona os detalhes como nós e as arestas para o backend
backend_details = [
    ('Autenticação\nGestão de Usuários', 'box'),
    ('Serviços\nTradução', 'box'),
    ('Serviços\nEnsino', 'box'),
    ('Reconhecimento\nEspacial', 'box'),
    ('Gerenciamento\nPacotes', 'box')
]

for detail, shape in backend_details:
    G.add_node(detail, label=detail, shape=shape)
    G.add_edge('Backend', detail)


ia_ml_details = [
    ('Visão\nComputacional', 'box'),
    ('Processamento\nLinguagem Natural', 'box'),
    ('Síntese\nde Voz', 'box'),
    ('Reconhecimento\nImagens/Objetos', 'box')
]

for detail, shape in ia_ml_details:
    G.add_node(detail, label=detail, shape=shape)
    G.add_edge('IA_ML', detail)


bd_armazenamento_details = [
    ('Banco de Dados\nUsuários/Perfis', 'box'),
    ('Banco de Dados\nEducacional', 'box'),
    ('Armazenamento\nTraduções', 'box'),
    ('Histórico\nde Configurações', 'box')
]

for detail, shape in bd_armazenamento_details:
    G.add_node(detail, label=detail, shape=shape)
    G.add_edge('BD_Armazenamento', detail)


conexoes = [
    ('Frontend', 'Backend'),
    ('Backend', 'IA_ML'),
    ('Backend', 'BD_Armazenamento'),
    ('Backend', 'Infraestrutura'),
    ('Backend', 'Seguranca'),
    ('Backend', 'Lançamento')
]

G.add_edges_from(conexoes)


pos = {
    'Frontend': (0, 0),
    'Backend': (2, 0),
    'IA_ML': (4, 1.5),
    'BD_Armazenamento': (4, -1.5),
    'Infraestrutura': (6, 1.5),
    'Seguranca': (6, -1.5),
    'Lançamento': (8, 0),
    'Autenticação\nGestão de Usuários': (2.5, 0.5),
    'Serviços\nTradução': (2.5, -0.5),
    'Serviços\nEnsino': (3.5, 0.5),
    'Reconhecimento\nEspacial': (3.5, -0.5),
    'Gerenciamento\nPacotes': (5.5, 0.5),
    'Visão\nComputacional': (7, 2),
    'Processamento\nLinguagem Natural': (7, 1.5),
    'Síntese\nde Voz': (7, 1),
    'Reconhecimento\nImagens/Objetos': (9, 2),
    'Banco de Dados\nUsuários/Perfis': (7, -2),
    'Banco de Dados\nEducacional': (7, -1.5),
    'Armazenamento\nTraduções': (7, -1),
    'Histórico\nde Configurações': (9, -2)
}


plt.figure(figsize=(16, 12))


nx.draw_networkx_nodes(G, pos, nodelist=[key for key in componentes.keys()], node_shape='o', node_size=4000, node_color="lightblue")
nx.draw_networkx_nodes(G, pos, nodelist=[detail for detail, shape in backend_details + ia_ml_details + bd_armazenamento_details], node_shape='s', node_size=3000, node_color="lightgreen")


nx.draw_networkx_edges(G, pos)

offset = 0.1
for key, (x, y) in pos.items():
    plt.text(x, y + offset, s=G.nodes[key]['label'], bbox=dict(facecolor='white', alpha=0.5), horizontalalignment='center', fontsize=9, fontweight="bold")

plt.title('Arquitetura de Soluções do Lookie')
plt.axis('off')
plt.show()
