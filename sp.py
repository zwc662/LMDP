import os, sys, inspect
import pickle
import numpy as np
import scipy.sparse as sparse

from mdp import mdp
from lmdp import lmdp
from graph import graph
from gridworld import gridworld


class sp():
    def __init__(self):
        self.G = graph()
        #MDP
        #self.M = mdp()
        #Linear MDP
        self.LM = None
        #Non-terminal states' reward
        self.R = 20

    def build_mdp_from_gridworld(self):
        D = gridworld(20)
        D.build_mdp()
        #D.M.optimal_policy(theta = np.array([1., 1., -1., -1.]))
        policy = 1 + np.random.randint(len(D.M.A) - 1, size = (len(D.M.S)))
         
        D.M.policy = np.eye(len(D.M.A))[policy]
        D.M.set_policy_random(init = True)

        self.LM = lmdp(source  = D.M)
  
    

    def shortest_path(self):
        self.G.build_from_mdp(self.LM)
        self.G.dijkstra()

        file = open('./data/sp', 'w')
        for s in self.LM.S:
            if self.G.P[s].list is not None:
                file.write("%d:%d:" % (s, self.G.P[s].len + 1))
                for s_ in self.G.P[s].list: 
                    file.write("%d " % s_)
                file.write("%d\n" % self.LM.S[-1])
    
    def shortest_path_lmdp(self):
        #for s in self.LM.S[:-2]:
        end = self.LM.S[20]
        if end == self.LM.S[20]:
            self.shortest_path_lmdp_to(end)

            
    
    def shortest_path_lmdp_to(self, end):
        #Reset all rewards
        self.LM.rewards = np.zeros([len(self.LM.S)]).astype(float)
        #Set all non-terminal rewards
        self.LM.rewards += self.R
        #Set terminal reward
        self.LM.rewards[self.LM.S[-1]] = 0.0
    
        #Reset terminal state transition
        self.LM.P[end] *= 0.0
        self.LM.P[end, self.LM.S[-1]] = 1.0
        self.LM.P[self.LM.S[-1]] *= 0.0
        self.LM.P[self.LM.S[-1], self.LM.S[-1]] = 1.0
    
        z = self.LM.discrete_solver__()
        print(z[0, len(self.LM.S) - 1])
        print(z[0, end])
        scale = 20.0/z[0, len(self.LM.S) - 1]
        print(scale)
        print(z[0, end] * scale)

        z_0, z_N = self.LM.discrete_solver()
        print(z_0[end])
        print(z_N[end])
        print(z_N[-1])
        print(z_N[0])
        if z_0[end] != 0.0:
            scale = (self.R - z_N[end])/z_0[end]
        print(scale)
        z_N = z_N + scale * z_0
        print(z_N[end])
        print(z_N[-1])
        print(z_N[0])

if __name__ == "__main__":
    sp = sp()
    sp.build_mdp_from_gridworld()
    sp.shortest_path()
    sp.shortest_path_lmdp()


