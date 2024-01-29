graph = {
    'A': ['B','D'],
    'B': ['E'],
    'C': ['A','G'],
    'D': ['F'],
    'E': ['G','C'],
    'F': ['C','G']
}
def  BFS(graph,Start,Goal):
     Visited = []
     queue = [[Start]]
     while queue :
         Path = queue.pop(0)
         node = Path[-1]
         if node in Visited :
             continue
         Visited.append(node)
         if node == Goal :
             return Path
         else :
             AdjacentNodes = graph.get(node,[])
             for node2 in AdjacentNodes :
              NewPath = Path.copy()
              NewPath.append(node2)
              queue.append(NewPath)

Solution = BFS(graph,'A','G')
print("the pqth by Breadth First Search Is" , Solution)