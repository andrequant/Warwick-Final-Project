import numpy as np
from abc import ABC, abstractmethod


class PDE():
    def __init__(self, diffusion_matrix,FD):
        pass
    
    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def density(self, x):
        pass


class PDE_test(PDE):

    def solve(self):
        pass

    def density(self, x, t):
        return 2
