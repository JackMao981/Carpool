import numpy as np
import math
from generate_schedule import *


def adjacent(g,node, n):
    """
    find all adjacent nodes of input node in g

    g: 2D array of numbers, the adjacency matrix
    node: int, the node whose neighber you wanna find

    return: a list of ints
    """
    result = []
    for i in range(n):
        if g[node][i] != 0:
            result.append(i)
    return result

def bfs(s, t, parent, g, n):
    """
    breadth first search algorithm

    s: int, source
    t: int, sink
    parent: list, the list of parents relative to the index that represent nodes
    g: 2D array of numbers, the adjacency matrix
    node: int, the node whose neighber you wanna find

    return: (bool, list), returns a boolean telling you if there is a path between
    s and t, and returns the path in the form of a parent list
    """
    visited = [False] * n
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for idx in adjacent(g, u, n):
            if visited[idx] == False:
                parent[idx] = u
                # print("parent",parent)
                if idx == t:
                    visited[idx] = True
                    return True, parent
                queue.append(idx)
                visited[idx] = True

    return False, parent

def edmond_karp(g,n):
    """
    Main function for edmond karp algorithm

    g: 2D array of numbers, the adjacency matrix
    node: int, the node whose neighber you wanna find
    n: int, number of nodes

    return: int, max flow
    """
    source = 0
    sink = len(g) - 1
    parent = [-1]*n
    max_flow = 0
    while(bfs(source, sink, parent, g, n)[0]):
        parent = bfs(source, sink, parent, g, n)[1]
        path_flow = math.inf
        s = sink
        while (s != source):
            path_flow = min(path_flow, g[parent[s]][s])
            # print(path_flow)
            s = parent[s]

        max_flow += path_flow

        v = sink

        while(v != source):
            u = parent[v]
            # print("graph",g[u][v], "path", path_flow)
            g[u][v] -= path_flow
            g[v][u] += path_flow
            v = parent[v]

    return max_flow

def print_g(g):
    """
    prints the graph, a helper function for clarity
    """
    for i in g:
        for j in i:
            print(round(j,2), "\t", end = '')
        print("\n")
# print(bfs(0,10,[-1]*n))
def print_schedule(g, p, n):
    """
    prints the schedule; row: people, columns: days
    """
    print( "\t\t", end = '')

    for i in range(1, n-1-p):
        print("day", i, "\t", end = '')

    print()
    for j in range(1, p+1):
        print("person", j, "\t", end = '')
        for i in range(p+1, n-1):
            print(round(g[i][j],2), "\t", end = '')
        print("\n")
