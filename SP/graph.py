import scipy as sci
import numpy as np
import math

import dtmc
				

class path():
    def __init__(self, start, end): 
        self.start = start
	self.end = end	
	self.len = 0
	self.list = [self.end]
            
    def add(self, s):
        self.list.append(s)
        self.len += 1 
    '''		
    def find_vertex(index):
        if index < len(path_list):
            return self.path_list[index]
        else:
            return None
    
    def find_index(vertex):
        for i in range(len(self.path_list)):
            if self.path_list[i].s == vertex.s:
                return i
        return None

    def find_next(vertex = None, index = None):
        if index is None:
            index = find_index(vertex)
        else:
            if index != find_index(vertex)
            raise Error
        return self.path_list[index + 1]	
    '''

class vertex():
    def __init__(self, s, W):
        ##state index##
        self.s = s

        ##set weights to all neighbors###
        self.W = W	
        ##set distance to the initial state to infinity##
        self.dist = float('inf')

        ##init the previous and next vertex in the shortes path	
        self.prev = None
        self.next = None
        self.token = False

class edge():
    def __init__(self, s, s_, W):
        self.s = s
        self.s_ = s_
        self.w = W[s, s_]
                        

class graph():
    def __init__(self):
        self.V = list()
        self.E = list()

        self.num_V = 0

        self.start = None
        self.P = {}
        self.P_rank = []

    def find_vertex(self, s): 
        for v in range(self.num_V):
            if self.V[v].s == s:
                return self.V[v]

    def build_from_dtmc(self, dtmc):
        ##turn transitions to weights by W=-log(P)
        W = - np.log(dtmc.T)
        #print(W)

        self.num_V = len(dtmc.S)
        ##init all the vertices
        for s in dtmc.S:
                        self.V.append(vertex(s, W[s,:]))
        ##init all the edges
                        for s_ in dtmc.S:
                                        self.E.append(edge(s, s_, W))	

        for t in dtmc.targets:
                        W[t] *= float('inf')
        for v in range(self.num_V):
                        W[self.V[v].s, self.V[v].s] = 0

        #print("Generated weight matrix")
        #print(W)

        ##set the start vetex
        self.start = dtmc.start
        self.V[self.start].token = True
        self.V[self.start].dist = 0.0
        #print("Start from ", self.V[self.start].s)


    def bfs(self, v):	
        #print("BFS ", v.s)
        for v_ in range(self.num_V):
            if v_ != v.s and v.W[v_] + v.dist < self.V[v_].dist:
                if self.V[v_].token is True:
                    raise Error
                self.V[v_].dist = v.W[v_] + v.dist
                #print("Update ",v_, " to ", self.V[v_].dist)
                self.V[v_].prev = v.s

    def dijkstra(self):		
        self.P[svelf.start] = path(self.start, self.start)
        self.P_rank = [self.start]
        self.bfs(self.V[self.start])
                        
        end = None
        while True:
            min_dist = float('inf')
            for v_ in self.V:
                #print(v_.s, v_.dist)
                if v_.dist < min_dist and v_.token is False:
                        min_dist = v_.dist
                        end = v_.s		
                                #print end
            if end == None:
                break
                #print end
                #print self.V[end].prev

            self.V[end].token = True
            self.P_rank.append(end)			
            self.P[end] = path(self.start, end)
            v_ = end
            while v_ != self.start:
                prev = self.V[v_].prev
                self.P[end].add(prev)
                v_ = prev
            #print(self.P[end].list)
                            
            self.bfs(self.V[end])
                    
            end = None
        #print(len(self.P.keys()))

            
            
            



                            
                      

