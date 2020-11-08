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
    A += (DA * discrete_laplacian(A) - A * B ** 2 + f * (1 - A)) * dt
    B += (DB * discrete_laplacian(B) + A * B ** 2 - (k + f) * B) * dt
    return A, B


def initial_conditions(s, a, b, r):
    A = r * np.random.random((s, s)) + (1 - r) * np.ones((s, s))
    B = r * np.random.random((s, s))
    # # centered square disturbance
    c = s // 2
    d = int(s / 60.0)
    A[c - d:c + d, c - d:c + d] = a
    B[c - d:c + d, c - d:c + d] = b
    return A, B


def animate(n, A, B, DA, DB, f, k, color):
    fig = plt.figure()
    frames = []
    for i in range(n):
        A, B = gray_scott_algorithm(A, B, DA, DB, f, k, dt=1.0)
        frame = plt.imshow(A, cmap=color)
        frames.append([frame])
    animation.ArtistAnimation(fig, frames, interval=100, blit=True, repeat=False)
    plt.axis('off')
    plt.show()


# name = ['parameter_to_plot', n, DA, DB, f, k, r, 'color']
spiral = ['A', 1000, 0.18, 0.082, 0.08, 0.05, 0.3, 'plasma']
frog = ['A', 1000, 0.16, 0.08, 0.060, 0.062, 0.3, 'summer']
bacteria = ['A', 1000, 0.12, 0.08, 0.06, 0.06, 0.3, 'twilight']
cheetah = ['B', 500, 0.08, 0.08, 0.06, 0.06, 0.3, 'copper']
brain = ['A', 1000, 0.16, 0.08, 0.06, 0.062, 0.3, 'ocean']
hyena = ['A', 1000, 0.14, 0.06, 0.035, 0.065, 0.2, 'copper']

A, B = initial_conditions(s=400, a=0.50, b=0.25, r=0.3)
animate(n=500, A=A, B=B, DA=0.08, DB=0.08, f=0.06, k=0.06, color='copper')
