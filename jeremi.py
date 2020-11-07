import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def discrete_laplacian(M):
    L = -4 * M
    L += np.roll(M, (0, -1), (0, 1))
    L += np.roll(M, (0, +1), (0, 1))
    L += np.roll(M, (-1, 0), (0, 1))
    L += np.roll(M, (+1, 0), (0, 1))
    return L


def gray_scott_algorithm(A, B, DA, DB, f, k, dt):
    LA = discrete_laplacian(A)
    LB = discrete_laplacian(B)
    diff_A = (DA * LA - A * B ** 2 + f * (1 - A)) * dt
    diff_B = (DB * LB + A * B ** 2 - (k + f) * B) * dt
    A += diff_A
    B += diff_B
    return A, B


def initial_conditions(n, a, b, r=0.3):
    A = r * np.random.random((n, n)) + (1 - r) * np.ones((n, n))
    B = r * np.random.random((n, n))
    # centered disturbance
    c = n // 2
    d = int(n / 100.0)
    A[c - d:c + d, c - d:c + d] = a
    B[c - d:c + d, c - d:c + d] = b
    return A, B


def pictures(n, A, B):
    frames = []
    for i in range(n):
        A, B = gray_scott_algorithm(A, B, DA=0.16, DB=0.08, f=0.050, k=0.062, dt=1.0)
        frame = plt.imshow(A, cmap='copper')
        frames.append([frame])
    return frames


A, B = initial_conditions(n=300, a=0.05, b=0.08)
fig = plt.figure()
animation.ArtistAnimation(fig, pictures(100, A, B), interval=100, blit=True, repeat=False)
plt.axis('off')
plt.show()
