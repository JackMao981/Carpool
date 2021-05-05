from carpool import *

def graph1():
    p = 4
    d = 5
    n = p + d + 2
    graph = np.zeros((n,n))
    graph[0][1] = 3/4
    graph[0][2] = 7/4
    graph[0][3] = 5/4
    graph[0][4] = 5/4
    graph[1][5] = 1
    graph[1][7] = 1
    graph[2][5] = 1
    graph[2][6] = 1
    graph[2][7] = 1
    graph[2][8] = 1
    graph[2][9] = 1
    graph[3][5] = 1
    graph[3][6] = 1
    graph[3][8] = 1
    graph[3][9] = 1
    graph[4][5] = 1
    graph[4][6] = 1
    graph[4][8] = 1
    graph[4][9] = 1
    graph[5][10] = 1
    graph[6][10] = 1
    graph[7][10] = 1
    graph[8][10] = 1
    graph[9][10] = 1
    return graph,p,n

def graph2():

    p = 4
    d = 5
    n = p + d + 2
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
    return g,p,n



def graph4():

    p = 4
    d = 5
    n = p + d + 2
    g = np.zeros((n,n))
    g[0][1] = 0
    g[0][2] = 0
    g[0][3] = 0
    g[0][4] = 0
    g[5][10] = 1
    g[6][10] = 1
    g[7][10] = 1
    g[8][10] = 1
    g[9][10] = 1
    return g,p,n

def graph5():

    p = 4
    d = 5
    n = p + d + 2
    g = np.zeros((n,n))
    g[0][1] = 5/4
    g[0][2] = 5/4
    g[0][3] = 5/4
    g[0][4] = 5/4
    g[1][5] = 1
    g[1][6] = 1
    g[1][7] = 1
    g[1][8] = 1
    g[1][9] = 1
    g[2][5] = 1
    g[2][6] = 1
    g[2][7] = 1
    g[2][8] = 1
    g[2][9] = 1
    g[3][5] = 1
    g[3][6] = 1
    g[3][7] = 1
    g[3][8] = 1
    g[3][9] = 1
    g[4][5] = 1
    g[4][6] = 1
    g[4][7] = 1
    g[4][8] = 1
    g[4][9] = 1
    g[5][10] = 1
    g[6][10] = 1
    g[7][10] = 1
    g[8][10] = 1
    g[9][10] = 1
    return g,p,n

def run(graph, p, n):
    edmond_karp(graph, n)
    print_schedule(graph, p, n)



"""
THESE ARE OUR TEST CASES

case 1: deterministic graph from our presentation

case 2: deterministic graph from the document

case 3: randomly generated graph

case 4: nobody needs carpool

case 5: everyone needs it everyday
"""

print("Case 1: Deterministic Graph 1 Carpool\n")
g1,p1,n1 = graph1()
print("Network Flow Adjacency Matrix:\n")
print_g(g1)
print("Case 1:Deterministic Graph 1 Driving Schedule\n")
run(g1,p1,n1)

print("Case 2: Deterministic Graph 2 Carpool\n")
g2,p2,n2 = graph2()
print("Network Flow Adjacency Matrix:\n")
print_g(g2)
print("Case 2: Deterministic Graph 2 Driving Schedule\n")
run(g2,p2,n2)

print("Case 3: Random Graph Carpool\n")
rng_p = 4
rng_d = 5
rng_n = rng_p + rng_d + 2
graph = generate(rng_p,rng_d)
print("Network Flow Adjacency Matrix:\n")
print_g(graph)
print("Case 3: Random Graph Driving Schedule\n")
run(graph, rng_p, rng_n)

print("Case 4: No one needs the carpool\n")
g4,p4,n4 = graph4()
print("Network Flow Adjacency Matrix:\n")
print_g(g4)
print("Case 2: Deterministic Graph 2 Driving Schedule\n")
run(g4,p4,n4)

print("Case 5: Everyone needs the carpool\n")
g5,p5,n5 = graph5()
print("Network Flow Adjacency Matrix:\n")
print_g(g5)
print("Case 2: Deterministic Graph 2 Driving Schedule\n")
run(g5,p5,n5)
