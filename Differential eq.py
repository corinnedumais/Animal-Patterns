# This is a test

import numpy as np
import matplotlib.pyplot as plt


def laplacian(M):
    """Get the discrete Laplacian of matrix M"""
    L = -4 * M
    L += np.roll(M, (0, -1), (0, 1))
    L += np.roll(M, (0, +1), (0, 1))
    L += np.roll(M, (-1, 0), (0, 1))
    L += np.roll(M, (+1, 0), (0, 1))

    return L


def gray_scott_update(A, B, DA, DB, f, k, delta_t):
    """
    Updates a concentration configuration according to a Gray-Scott model
    with diffusion coefficients DA and DB, as well as feed rate f and
    kill rate k.
    """

    # Let's get the discrete Laplacians first
    LA = laplacian(A)
    LB = laplacian(B)

    # Now apply the update formula
    diff_A = (DA * LA - A * B ** 2 + f * (1 - A)) * delta_t
    diff_B = (DB * LB + A * B ** 2 - (k + f) * B) * delta_t

    A += diff_A
    B += diff_B

    return A, B


def get_square_ci(N, random_influence=0.3):
    """
    Initialize a concentration configuration. N is the side length
    of the (N x N)-sized grid.
    `random_influence` describes how much noise is added.
    """

    # We start with a configuration where on every grid cell
    # there's a lot of chemical A, so the concentration is high
    A = (1 - random_influence) * np.ones((N, N)) + random_influence * np.random.random((N, N))

    # Let's assume there's only a bit of B everywhere
    B = random_influence * np.random.random((N, N))

    # Now let's add a disturbance in the center
    N2 = N // 2
    r = int(N / 10.0)

    A[N2 - r:N2 + r, N2 - r:N2 + r] = 0.50
    B[N2 - r:N2 + r, N2 - r:N2 + r] = 0.25

    return A, B


def get_stripe_ci(N, random_influence=0.3):
    # We start with a configuration where on every grid cell
    # there's a lot of chemical A, so the concentration is high
    A = (1 - random_influence) * np.ones((N, N)) + random_influence * np.random.random((N, N))

    # Let's assume there's only a bit of B everywhere
    B = random_influence * np.random.random((N, N))

    A[int(N/2):int(N/2) + 5, :] = 0.75
    B[int(N/2):int(N/2) + 5, :] = 0.25

    A[int(N/2):int(N/2) + 5, :] = 0.75
    B[int(N/2):int(N/2) + 5, :] = 0.25

    return A, B


def draw(A, B):
    """draw the concentrations"""
    fig, ax = plt.subplots(1, 2, figsize=(5.65, 4))
    ax[0].imshow(A, cmap='Greys'), ax[0].set_title('A'), ax[0].axis('off')
    ax[1].imshow(B, cmap='Greys'), ax[1].set_title('B'), ax[1].axis('off')
    plt.show()


# A, B = get_initial_configuration(200)
# draw(A, B)

# update in time
delta_t = 1.0

# Diffusion coefficients
DA = 0.16
DB = 0.08

# define feed/kill rates
f = 0.050
k = 0.062

# grid size
N = 200

# simulation steps
N_simulation_steps = 14000

A, B = get_stripe_ci(300)

for t in range(N_simulation_steps):
    A, B = gray_scott_update(A, B, DA, DB, f, k, delta_t)
    if t % 1000 == 0:
        draw(A, B)




