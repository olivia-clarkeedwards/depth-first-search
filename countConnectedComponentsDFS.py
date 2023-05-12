'''

Description: Prints number of connected components, 
and an array of which nodes belong to which components, 
based on given adjacency list. 
Author: Olivia Clarke-Edwards

'''
graph1 = [[1], [2], [3, 5], [2, 4], [2, 3], [2, 6], [5, 7, 8], [6], [6]]
graph2 = [[1], [0], [3, 4], [2, 4], [2, 3]]

def findComponents(g, n, count, components, visited): 
    
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i, g, count, components, visited)
    return count, components
    
    
def dfs(current, g, count, components, visited):
    
    visited[current] = True
    components[current] = count

    for next in g[current]:
        if not visited[next]:
            dfs(next, g, count, components, visited)


def test(g):
    n = len(g)
    count = 0
    components = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    print(findComponents(g, n, count, components, visited))

test(graph1)
test(graph2)
test([])

    


    


