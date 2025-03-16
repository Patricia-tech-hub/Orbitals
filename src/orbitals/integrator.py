from abc import ABC, abstractmethod

class Integrator(ABC):
    def __init__(self, equation, dt):
        self.equation = equation
        self.dt = dt
    
    @abstractmethod
    def step(self, t, state, dt):
        pass

class EulerIntegrator(Integrator):
    def step(self, t, state):
        derivatives = self.equation(t, state)
        new_state = [s + ds * self.dt for s, ds in zip(state, derivatives)]
        return t + self.dt, new_state