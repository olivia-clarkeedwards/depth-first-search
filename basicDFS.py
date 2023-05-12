'''

Description: Prints depth-first search based on given adjacency list. 
Author: Olivia Clarke-Edwards

'''

adjacency_graph = [[1], [2], [3, 5], [2, 4], [2, 3], [2, 6], [5, 7, 8], [6], [6]]
n = len(adjacency_graph)
visited = [False] * n

def dfs(current):
    if (visited[current]): 
       return
    
    print(current)

    visited[current] = True

    neighbours = adjacency_graph[current]
    for next in neighbours:
        dfs(next)


start_node = 0
dfs(start_node)