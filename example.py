from orbitals import OrbitalMotion

eq = OrbitalMotion(G=1.0, M=1.0)
t, state = 0, [1.0, 0.0, 0.0, 1.0] # (x, y, vx, vy)
# The __call__ method is called when we use the object as a function
derivatives = eq(t, state)
print(derivatives) # [0.0, 1.0, -1.0, 0.0]
