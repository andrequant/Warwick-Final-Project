import numpy as np
from abc import ABC, abstractmethod



class FundamentalDiagram():
    def __init__(self, params):
        self.params = params

    def __call__(self,density):
        return self.flux(density)
    
    @abstractmethod
    def flux(self, density):
        pass

    @abstractmethod
    def __str__(self):
        pass



class Greenshield(FundamentalDiagram):
    def __init__(self, params):
        super().__init__(params)
        self.v_max = self.params[0]
        self.p_max = self.params[1]
    
    def flux(self, density):
        return self.v_max * (1 - (density/self.p_max))
    
    def __str__(self):
        return "Greenshield"
    

    

class Bilinear(FundamentalDiagram):
    def __init__(self, params):
        super().__init__(params)
        self.v_max = self.params[0]
        self.p_max = self.params[1]
        self.p_critical = self.params[2]
    
    def flux(self, density):
        if density <= self.p_critical:
            return self.v_max * density
        else:
            return self.v_max * ((self.p_critical * self.p_max)/
                                 (self.p_max - self.p_critical)) * (1-(density/self.p_max))
        
    def __str__(self):
            return "Bilinear"
# Include others models