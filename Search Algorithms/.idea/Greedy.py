graph = {
    'A': [('C',3),('B',4),('E',7)],
    'B': [('A',4),('C',6),('D',5)],
    'C': [('A',3),('D',11),('B',6),('E',8)],
    'D': [('B',5),('C',11),('E',2),('G',10),('F',2)],
    'E': [('A',7),('C',8),('D',2),('G',5)],
    'G': [('E',5),('D',10),('F',3)],
    'F': [('G',3),('D',2)]
}
H_table = {
    'C' : 56,
    'B' : 30 ,
    'A' : 28,
    'D' : 60,
    'G' : 36,
    'E': 44,
    'F': 0 ,
}
def Path_H_Cost (path):
    G_Cost = 0
    for (node,cost) in path :
     G_Cost += cost
    last_node = path[-1][0]
    H_Cost = H_table[last_node]
    return H_Cost,last_node
def Greedy(gragh,start,goal) :
    Visted = []
    queue = [[(start , 0)]]
    while queue :
        queue.sort(key=Path_H_Cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in Visted :
            continue
        Visted.append(node)
        if node== goal :
            return path
        else :
            adjacent_nodes = gragh.get(node , [])
            for(node2,cost) in adjacent_nodes :
                new_path = path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)

solution = Greedy(graph,'A','F')
print('Solution by Greedy is ',solution)
print('Cost of Soultion is ' , Path_H_Cost(solution)[0])