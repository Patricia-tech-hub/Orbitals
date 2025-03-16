from abc import ABC, abstractmethod
import numpy as np

class DifferentialEquation(ABC):
    @abstractmethod
    def __call__(self, t, state):
        pass
    
class OrbitalMotion(DifferentialEquation):
    def __init__(self, G, M):
        self.G = G
        self.M = M
        pass
    
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
        r = np.sqrt(x**2 + y**2)
        ax = -self.G * self.M * x / r**3
        ay = -self.G * self.M * y / r**3
        return [vx, vy, ax, ay]
