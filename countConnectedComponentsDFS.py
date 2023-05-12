'''

Description: Prints number of connected components based on given adjacency list. 
Author: Olivia Clarke-Edwards

'''
adjacency_graph = [[1], [2], [3, 5], [2, 4], [2, 3], [2, 6], [5, 7, 8], [6], [6]]
n = len(adjacency_graph)
count = 0
components = [[] for _ in range(n)]
visited = [False for _ in range(n)]

def findComponents(count): 
    
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return count
    
    
def dfs(current):
    
    visited[current] = True
    components[current] = count

    for next in adjacency_graph[current]:
        if not visited[next]:
            dfs(next)


def main():
  
    print(findComponents(count))

main()

    


    


