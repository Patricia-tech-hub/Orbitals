import orbitals

eq = OrbitalMotion(G=1.0, M=1.0)
dt = 0.001
integrator = EulerIntegrator(eq, dt)
t, state = 0, [1.0, 0.0, 0.0, 1.0] # (x, y, vx, vy)
for _ in range(100):
   t, state = integrator.step(t, state)
print(f"t={t:.2f}, x={state[0]:.3f}, y={state[1]:.3f}")