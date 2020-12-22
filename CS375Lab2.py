# CS375 Lab 2, Fall 2020, due September 11
import random
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


def genRandomGraph(n, p):

    # Helper function to create edge for undirected graph
    def addEdge(G, v, w):
        G[v].append(w)
        G[w].append(v)

    G = [[] for i in range(n)]

    # initalizing graph
    for i in range(n):
        q = float('inf')
        for j in range(n):
            if i < j:
                q = random.random()
            if q < p:
                addEdge(G, i, j)
    return G


def largestComponent(G, t, n):

    # Depth First Search Helper Function O(V + E)
    def dfs(temp, v, visited):
        visited[v] = True
        temp.append(v)

        for i in G[v]:
            if not visited[i]:
                temp = dfs(temp, i, visited)
        return temp

    visited = []
    cc = []
    for i in range(n):
        visited.append(False)
    for v in range(n):
        if not visited[v]:
            temp = []
            vertices = len(dfs(temp, v, visited))
            if vertices >= t:
                return 1
    return 0

    # def dfs(G, start=0):
    #     visited = [False] * len(G[0])
    #     stack = []
    #     stack.append(start)
    #
    #     while stack:
    #         v = stack.pop()
    #         if not visited[v]:
    #             visited[v] = True
    #             for neighbor in G[v]:
    #                 stack.append(neighbor)
    #             if len(stack) >= t:
    #                 print(len(stack))
    #     return 0

    # G = csr_matrix(G)
    # n_components, labels = connected_components(csgraph=G, directed=False, return_labels=True)
    #
    # if n_components >= t:
    #     return 1
    # else:
    #     return 0


def main():
    n = 40

    data = []
    listC = []

    for c in range(2, 32, 2):
        c /= 10
        listC.append(c)
        p = c/float(n)
        percentage = 0
        for i in range(500):
            graph = genRandomGraph(n, p)
            if largestComponent(graph, 30, n) == 1:
                percentage += 1
        percentage /= 500
        data.append(percentage)

    plt.plot(listC, data)
    plt.xlabel('c')
    plt.ylabel('Percentage')
    plt.show()


main()
