graph = {
    'A': [('B',1),('D',2),('S',2)],
    'B': [('A',1),('C',4),('E',5)],
    'C': [('B',4)],
    'D': [('A',2),('S',5),('E',2)],
    'E': [('B',5),('D',2),('F',4)],
    'G': [('F',3)],
    'F': [('G',3),('E',4)],
    'S': [('A',2),('D',5)]
}
H_table = {
    'C' : 4.0,
    'B' : 6.7 ,
    'A' : 10.4,
    'D' : 8.9,
    'G' : 0,
    'E': 6.9,
    'F': 3.0 ,
    'S': 11.0,
}
def Path_F_Cost (path):
    G_Cost = 0
    for (node,cost) in path :
        G_Cost += cost
    last_node = path[-1][0]
    H_Cost = H_table[last_node]
    F_cost = G_Cost + H_Cost
    return F_cost,last_node
def A_Star(gragh,start,goal) :
    Visted = []
    queue = [[(start , 0)]]
    while queue :
        queue.sort(key=Path_F_Cost)
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

solution = A_Star(graph,'S','G')
print('Solution by A* is  ',solution)
print('Cost of Soultion is ' , Path_F_Cost(solution))