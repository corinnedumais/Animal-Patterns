import numpy as np
from sympy.physics.quantum import Ket, Bra

# algo needs to tell if quantum state is entangled or separable
# input: 4x4 array
# must always detect a separable state but can occasionally fail to detect an entangled state
# kronecker product np.kron(a, b)


def quantum_state(M):
    if np.linalg.matrix_rank(M) == 1.0:
        print('The quantum state is not entangled.')
        return True
    else:
        print('The quantum state is entangled.')
        return False


state1 = 1 / np.sqrt(2) * np.array([1, 1, 0, 0])
state2 = 1 / np.sqrt(2) * np.array([1, 0, 0, 1])
state11 = 0.5 * np.array([[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]])
state12 = 0.5 * np.array([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])

quantum_state(state2)
