from abc import ABC, abstractmethod

class DifferentialEquation(ABC):
    '''Represents a system of differential equations'''
    @abstractmethod
    # The dunder method __call__ enables the parenthesis operator, so we can call the object as if it were a function.
    def __call__(self, t, state):
        pass
    
    def __init__(self, f, x0, y0, h):
        self.f = f
        self.x = x0
        self.y = y0
        self.h = h

    def f(t, state):
        '''Represents the system of equations governing motion'''
        raise NotImplementedError
    
    def step(self):
        self.y += self.h * self.f(self.x, self.y)
        self.x += self.h

    def solve(self, x):
        while self.x < x:
            self.step()
        return self.y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
class OrbitalMotion(DifferentialEquation):
    '''Represents Newton’s equations of motion under gravity'''

    def __init__(self, x0, y0, h):
        super().__init__(self.f, x0, y0, h)
    
    def f(self, t, state):
        x, y, vx, vy = state
        r = (x**2 + y**2)**0.5
        a = -1 / r**3
        return [vx, vy, a*x, a*y]
    
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