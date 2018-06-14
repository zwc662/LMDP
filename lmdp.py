import sys
import numpy as np

from mdp import mdp





class lmdp(object, mdp):
    def __init__(self, source = None, num_S = None, num_A = None):
        if source is not None:
            self.__dict__.update(source.__dict__)
        elif (num_S is not None) and (num_A is not None):
            self.S = range(num_S + 2)
            self.A = range(num_A)
        else:
            self.S = None
            self.A = None

    def discrete_solver(self): 
        diag_exp_qN = np.diag(np.exp(self.rewards[:-1]))
        assert diag_exp_qN.shape == (len(self.S) - 1, len(self.S) - 1)
        #print(diag_exp_qN)

        P_NN = self.P[:-1, :-1]
        assert P_NN.shape == diag_exp_qN.shape
        #print(P_NN)

        a = diag_exp_qN - P_NN
        assert a.shape == (len(self.S) - 1, len(self.S) - 1)
    
        P_NT = np.reshape(self.P[:-1, -1], (len(self.S) - 1, 1))
        assert P_NT.shape == (len(self.S) - 1, 1)
        #print(P_NT)

        exp_neg_qT = np.reshape(np.exp(-1.0 * self.rewards[-1:]), (1, 1))
        assert exp_neg_qT.shape == (1,1)
        #print(exp_neg_qT)

        b = np.dot(P_NT, exp_neg_qT)
        assert b.shape == (len(self.S) - 1, 1)


        z_0 = np.linalg.solve(a, b * 0.0)
        z_N = np.linalg.solve(a, b)

        return z_0, z_N

    def discrete_solver_(self): 
        M = np.dot(np.diag(np.exp(-1.0 * self.rewards)), self.P + 1.0e-5) 



        z_N = np.linalg.solve(M - np.eye(len(self.S)), np.zeros((len(self.S))))

        return z_N

    def discrete_solver__(self):
        M = np.dot(np.diag(np.exp(-1.0 * self.rewards)), self.P + 1.0e-5) 
        eigen_vals, eigen_vecs = np.linalg.eig(M)
        
        z_N = eigen_vecs[np.argmax(np.linalg.norm(eigen_vals - 1.0, ord = 2))] 
        return z_N

