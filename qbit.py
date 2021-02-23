import random
import numpy as np
import math

class Qbit:
    def __init__(self, state=None):
        # state = np.array([a,b]) = a|0> + b|1>
        # The state can be a unitary numpy vector in 2d
        # Qbit described in the standard basis |0> |1>

        if state is not None:
            self.state = np.asarray(state, dtype='complex') / np.linalg.norm(np.asarray(state))
        else:
            # If no state is given, a random initialization is given
            x = np.random.standard_normal(2) + np.random.standard_normal(2)*1j
            self.state = x / np.linalg.norm(x)

    def measure(self):
        # Measure the qbit
        # Returns 0 with probability self.state[0]^2 and 1 with prob. self.state[1]^2
        r = np.random.random()
        if r < np.abs(self.state[0])**2:
            # The qbit is left on the |0> state
            self.state = np.array([1,0])
        else:
            # the qbit is left on the |1> state
            self.state = np.array([0,1])

if __name__ == '__main__':
    N = 1000
    count = 0
    print(f"Sampling {N} random Qbits and measuring how many are in state |0>")
    for _ in range(N):
        qbit1 = Qbit()
        qbit1.measure()
        if np.all(qbit1.state == np.array([1,0])):
            count += 1
    print(count/N)