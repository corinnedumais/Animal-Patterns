# This is a test

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle


def laplacian(M):
    """Get the discrete Laplacian of matrix M"""
    L = -4 * M
    L += np.roll(M, (0, -1), (0, 1))
    L += np.roll(M, (0, +1), (0, 1))
    L += np.roll(M, (-1, 0), (0, 1))
    L += np.roll(M, (+1, 0), (0, 1))
    return L


def update(A, B, DA, DB, f, k, delta_t):
    A += (DA * laplacian(A) - A * B ** 2 + f * (1 - A)) * delta_t
    B += (DB * laplacian(B) + A * B ** 2 - (k + f) * B) * delta_t
    return A, B


def get_square_ci(N, random_influence=0.3):
    A = (1 - random_influence) * np.ones((N, N)) + random_influence * np.random.random((N, N))
    B = random_influence * np.random.random((N, N))

    # Now let's add a disturbance in the center
    N2 = N // 2
    r = int(N / 30.0)

    A[N2 - r:N2 + r, N2 - r:N2 + r] = 0.50
    B[N2 - r:N2 + r, N2 - r:N2 + r] = 0.25

    return A, B


def get_impulse_ci(N, random_influence=0.3):
    A = (1 - random_influence) * np.ones((N, N)) + random_influence * np.random.random((N, N))
    B = random_influence * np.random.random((N, N))

    # Now let's add a disturbance in the center
    N2 = N // 2
    r = int(N / 10.0)

    A[N2 - r:N2 + r, N2 - r:N2 + r] = 0.50
    B[N2 - r:N2 + r, N2 - r:N2 + r] = 0.25


def get_guepard(N, random_influence=0.3):
    A = (1 - random_influence) * np.ones((N, N)) + random_influence * np.random.random((N, N))
    B = random_influence * np.random.random((N, N))

    A[int(N/2):int(N/2) + 5, :] = 0.6
    B[int(N/2):int(N/2) + 5, :] = 0.25

    A[:, int(N / 2):int(N / 2) + 5] = 0.6
    B[:, int(N / 2):int(N / 2) + 5] = 0.25

    return A, B


def draw(A, B):
    fig, ax = plt.subplots(1, 2, figsize=(5.65, 4))
    ax[0].imshow(A, cmap='summer'), ax[0].set_title('A'), ax[0].axis('off')
    ax[1].imshow(B, cmap='summer'), ax[1].set_title('B'), ax[1].axis('off')
    plt.show()


# update in time
delta_t = 1.0

# Diffusion coefficients
DA = 0.18
DB = 0.082

# define feed/kill rates
f = 0.08
k = 0.05

# grid size
N = 200

# simulation steps
N_simulation_steps = 10000

A, B = get_square_ci(200)

ims = []

for t in range(N_simulation_steps):
    if t % 10 == 0:
        A, B = update(A, B, DA, DB, f, k, delta_t)
        ims.append([plt.imshow(A)])

fig = plt.figure()

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat=False)

plt.show()



