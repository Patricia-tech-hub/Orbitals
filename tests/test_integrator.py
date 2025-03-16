from orbitals import DifferentialEquation, EulerIntegrator

def test_euler():
    factor = 5.0
    initial = 1.0
    dt = 0.01

    class Eq(DifferentialEquation):
        def __call__(self, t, state):
            return [factor * state[0]]

    eq = Eq()
    # Alternative:
    # eq = lambda t, state: [factor * state[0]]
    i = EulerIntegrator(eq, dt=dt)
    t, state = 0, [initial]
    assert i.step(t, state) == (dt, [initial + factor * initial * dt])