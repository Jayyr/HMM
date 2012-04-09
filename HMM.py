import sys, math

class HMM:
    def __init__(self, E, S, theta, marginal):
        self.emission = E
        self.stateSpace = S
        self.parameters = theta
        self.marginal = marginal
        
    def a(self,k,l):
        return self.parameters[a][k][l]
    def e(self k,b):
        return self.parameters[e][k][b]
    def p(self, k):
        return self.marginal[k]
    
