import networkx as nx 


g = nx.Graph()

g.add_nodes_from([1,2,3,4,5])

nx.draw(g)

#def Djikstra(g, start)