graph = {
    'A': ['B','D'],
    'B': ['E'],
    'C': ['A','G'],
    'D': ['F'],
    'E': ['G','C'],
    'F': ['C','G']
}
def DFS(graph,Start,Goal):
    Visited = []
    stack = [[Start]]
    while stack :
        Path = stack.pop()
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
              stack.append(NewPath)

Solution = DFS(graph,'A','G')
print("the path by Depht First Search Is" , Solution)