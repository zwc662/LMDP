import os, sys, inspect
import numpy as np
import scipy.sparse as sparse

from mdp import mdp
from graph import graph
from gridworld import gridworld







if __name__ == "__main__":
    D = gridworld()
    D.build_mdp_from_file()
    D.M.optimal_policy(theta = np.array([1., 1., -1., -1.]))
    print(D.M.S)

    G = graph()
    G.build_from_mdp(D.M)
    G.dijkstra()
    for s in D.M.S:
        print(G.P[s].list)

