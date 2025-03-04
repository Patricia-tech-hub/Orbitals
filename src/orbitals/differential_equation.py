class DifferentialEquation:
    def __init__(self, f, x0, y0, h):
        self.f = f
        self.x = x0
        self.y = y0
        self.h = h

    
    def step(self):
        self.y += self.h * self.f(self.x, self.y)
        self.x += self.h

    def solve(self, x):
        while self.x < x:
            self.step()
        return self.y

    def __str__(self):
        return f"({self.x}, {self.y})"