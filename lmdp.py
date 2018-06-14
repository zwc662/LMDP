import sys
from mdp import mdp





class lmdp(object, mdp):
    def __init__(self, source = None, num_S = None, num_A = None):
        if source is not None:
            self.__dict__.update(source.__dict__)
        else:
            self.S = range(num_S + 2)
            self.A = range(num_A)

    @classmethod
    def config(cls, num_S, num_A):
        return cls(None, num_S = num_S, num_A = num_A)


if __name__ == "__main__":
    

