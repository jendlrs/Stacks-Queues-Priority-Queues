import networkx as nx
from graph import (City, 
load_graph, 
breadth_first_traverse, 
breadth_first_search as bfs,
)
from graph import shortest_path
from graph import connected
from graph import (
    City,
    load_graph,
    depth_first_traverse,
    depth_first_search as dfs,
)

#graph = nx.nx_agraph.read_dot("roadmap.dot")
#nodes, graph = load_graph("roadmap.dot", City.from_dict)

#Displaying the nodes for particular City
#print(nodes["london"]) #print the dictionary for particular city
#Displaying Graph Variables
#print(graph) #Graph of the specific city

#Determining Immediate Neighbors:
#for neighbor in graph.neighbors(nodes["london"]):
 #   print(neighbor.name)

#Determining the Distance from the given City:")
#for neighbor, weights in graph[nodes["london"]].items():
 #   print(weights["distance"], neighbor.name)

#Sorted cities by one or more weights
#def sort_by(neighbors, strategy):
 #   return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

#def by_distance(weights):
 #   return float(weights["distance"])

#for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
 #   print(f"{weights['distance']:>3} miles, {neighbor.name}")

#Finding the places in UK that has been granted city status in 2oth century: ")
#def is_twentieth_century(year):
 #  return year and 1901 <= year <= 2000

#Sorted Neighbors and visit first the cities with higher latitude
#def order(neighbors):
 #   def by_latitude(city):
  #      return city.latitude
   # return iter(sorted(neighbors, key=by_latitude, reverse=True))
    
#nodes, graph = load_graph("roadmap.dot", City.from_dict)
#for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
 #   print("📍", node.name)
  #  if is_twentieth_century(node.year):
   #     print("Found:", node.name, node.year)
    #    break
#else:
 #   print("Not found")

#breadth-first search and traversal implementations
#def is_twentieth_century(city):
 #   return city.year and 1901 <= city.year <= 2000

#nodes, graph = load_graph("roadmap.dot", City.from_dict)
#city = bfs(graph, nodes["edinburgh"], is_twentieth_century)

#for city in breadth_first_traverse(graph, nodes["edinburgh"]):
 #   print(city.name)

#Enumerate the shortest paths between two cities.
nodes, graph = load_graph("roadmap.dot", City.from_dict)

#city1 = nodes["aberdeen"]
#city2 = nodes["perth"]

#for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
 #   print(f"{i}.", " → ".join(city.name for city in path))

#" → ".join(city.name for city in shortest_path(graph, city1, city2))

#function for getting the reverse lattitude of the city.
#def by_latitude(city):
 #   return -city.latitude

#Path that prioritize the neighbors with a higher latitude
#" → ".join(
 #   city.name
  #  for city in shortest_path(graph, city1, city2, by_latitude)
#)

#Connected or Not
#from graph import connected
#print(connected(graph, nodes["belfast"], nodes["glasgow"]))

#print(connected(graph, nodes["belfast"], nodes["derry"]))

#Depth-First Search Using LIFO Queue

#def is_twentieth_century(year):
 #   return year and 1901 <= year <= 2000

#nodes, graph = load_graph("roadmap.dot", City.from_dict)
#for node in nx.dfs_tree(graph, nodes["edinburgh"]):
 #   print("📍", node.name)
  #  if is_twentieth_century(node.year):
   #     print("Found:", node.name, node.year)
    #    break
#else:
 #   print("Not found")

def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
city = dfs(graph, nodes["edinburgh"], is_twentieth_century)
print(city.name)
