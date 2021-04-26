import numpy as np

n = 11
g = np.zeros((n,n))
g[0][1] = 11/12
g[0][2] = 7/12
g[0][3] = 23/12
g[0][4] = 19/12
g[1][5] = 1
g[1][6] = 1
g[1][7] = 1
g[2][5] = 1
g[2][7] = 1
g[3][5] = 1
g[3][6] = 1
g[3][7] = 1
g[3][8] = 1
g[3][9] = 1
g[4][6] = 1
g[4][7] = 1
g[4][8] = 1
g[4][9] = 1
g[5][10] = 1
g[6][10] = 1
g[7][10] = 1
g[8][10] = 1
g[9][10] = 1

def ford_fulkerson(source, sink):
    pass
def adjacent(node):
    result = []
    for i in range(n):
        if g[node][i] != 0:
            result.append(i)
    return result

def bfs(s, t, parent):
    visited = [False] * n
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for idx in adjacent(u):
            if visited[idx] == False:
                if idx == t:
                    print(parent)
                    visited[idx] = True
                    return True
                queue.append(idx)
                visited[idx] = True
                parent[idx] = u

    return False

print(bfs(0,10,[-1]*n))
