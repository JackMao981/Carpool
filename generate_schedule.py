import numpy as np


def random_sched(p, d):
    return np.random.randint(2, size=(p,d))


def perc_drive(p,d,rand):
    drive = np.zeros((p, d))
    denoms = np.sum(rand, axis=0)

    for p_idx, i in enumerate(rand):
        for day_idx, j in enumerate(i):
            if denoms[day_idx] != 0:
                drive[p_idx][day_idx] = j / denoms[day_idx]
            else:
                drive[p_idx][day_idx] = 0
    return drive


def generate(p, d):
    n = p + d + 2 # num of nodes: people, days, source & sink
    g = np.zeros((n,n))

    # days to sink capacities
    for i in range(d):
        g[i+p+1][n-1] = 1

    # person to day
    rand = random_sched(p, d)
    for i, row in enumerate(rand):
        for j, _ in enumerate(row):
            if rand[i][j] != 0:
                g[i+1][j+p+1] = 1

    # person driving capacities
    driv = perc_drive(p, d, rand)
    for idx,i in enumerate(np.sum(driv, axis=1)):
        g[0][idx+1] = i

    return g
# p = 4
# d = 5
# n = p + d + 2
# g = np.zeros((n,n))
# g[0][1] = 11/12
# g[0][2] = 7/12
# g[0][3] = 23/12
# g[0][4] = 19/12
# g[1][5] = 1
# g[1][6] = 1
# g[1][7] = 1
# g[2][5] = 1
# g[2][7] = 1
# g[3][5] = 1
# g[3][6] = 1
# g[3][7] = 1
# g[3][8] = 1
# g[3][9] = 1
# g[4][6] = 1
# g[4][7] = 1
# g[4][8] = 1
# g[4][9] = 1
# g[5][10] = 1
# g[6][10] = 1
# g[7][10] = 1
# g[8][10] = 1
# g[9][10] = 1



# graph = generate(3,5)
# print(graph)
