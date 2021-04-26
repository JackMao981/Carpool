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





graph = generate(3,5)
print(graph)