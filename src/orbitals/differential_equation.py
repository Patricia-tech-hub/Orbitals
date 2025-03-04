from abc import ABC, abstractmethod

class DifferentialEquation(ABC):
    '''Represents a system of differential equations'''
    @abstractmethod
    # The dunder method __call__ enables the parenthesis operator, so we can call the object as if it were a function.
    def __call__(self, t, state):
        pass
    
import numpy as np
class OrbitalMotion(DifferentialEquation):
    def __init__(self, G, M):
        # Your code here
    
    def __call__(self, t, state):
        """Return the derivatives of the state vector.
        The state represents the position and velocity of the planet in
        2D space, so state = [x, y, vx, vy]
        Parameters:
        t (float): Time
        state (list): State vector [x, y, vx, vy]
        Returns:
        list: Derivatives [vx, vy, ax, ay]
        """
    x, y, vx, vy = state
    # Your code here
    return [vx, vy, ax, ay]

class Integrator():
    '''Integrates a differential equation'''
    
    def __init__(self, diff_eq):
        self.diff_eq = diff_eq
        
    def solve(self, x):
        return self.diff_eq.solve(x)
    
    def step(self, state, dt):
        '''Integrates the differential equation by a small time step'''
        self.diff_eq.x = state[0]
        self.diff_eq.y = state[1]
        self.diff_eq.h = dt
        self.diff_eq.step()
        return [self.diff_eq.x, self.diff_eq.y]

class EulerIntegrator(Integrator):
    '''Integrates a differential equation using the Euler method'''
    
    def solve(self, x):
        state = [self.diff_eq.x, self.diff_eq.y]
        while self.diff_eq.x < x:
            state = self.step(state, self.diff_eq.h)
        return state