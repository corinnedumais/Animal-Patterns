import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def discrete_laplacian(M):
    """
    Computes the discrete laplacian of an array
    """
    L = -4 * M
    L += np.roll(M, (0, -1), (0, 1))
    L += np.roll(M, (0, +1), (0, 1))
    L += np.roll(M, (-1, 0), (0, 1))
    L += np.roll(M, (+1, 0), (0, 1))
    return L


def update_algorithm(A, B, DA, DB, f, k, dt):
    """
    Updates A and B based on the Gray-Scott algorithm for Reaction Diffusion
    :param A: component A array
    :param B: component B array
    :param DA: component A coefficient
    :param DB: component B coefficient
    :param f: feed rate
    :param k: kill rate
    :param dt: time element
    :return: updated numpy arrays of components A and B
    """
    A += (DA * discrete_laplacian(A) - A * B ** 2 + f * (1 - A)) * dt
    B += (DB * discrete_laplacian(B) + A * B ** 2 - (k + f) * B) * dt
    return A, B


def initial_conditions(s, a, b, r):
    """
    Sets the initial conditions of components A et B
    :param s: size of the sample / image to plot
    :param a: disturbance value for component A
    :param b: disturbance value for component B
    :param r: random state of component distribution
    :return: numpy arrays of initial states for components A and B
    """
    A = r * np.random.random((s, s)) + (1 - r) * np.ones((s, s))
    B = r * np.random.random((s, s))
    # centered square disturbance
    c = s // 2
    d = int(s / 60.0)
    A[c - d:c + d, c - d:c + d] = a
    B[c - d:c + d, c - d:c + d] = b
    return A, B


def plot(n, A, B, DA, DB, f, k, color):
    """
    Plots the last update of component A or B
    """
    for i in range(n):
        A, B = update_algorithm(A, B, DA, DB, f, k, dt=1.0)
    plt.figure()
    plt.imshow(B, cmap=color)
    plt.axis('off')
    plt.show()


def animate(n, A, B, DA, DB, f, k, color):
    """
    Animates the updates of component A or B
    """
    fig = plt.figure()
    frames = []
    for i in range(n):
        A, B = update_algorithm(A, B, DA, DB, f, k, dt=1.0)
        frame = plt.imshow(B, cmap=color)
        frames.append([frame])
    animation.ArtistAnimation(fig, frames, interval=100, blit=True, repeat=False)
    plt.axis('off')
    plt.show()


# ----------------------------------------------------------------------------------------------------------------------

# patterns to plot or animate
# name = [n, DA, DB, f, k, r, 'color']
spiral = [1000, 0.18, 0.082, 0.08, 0.05, 0.3, 'plasma']
frog = [1000, 0.16, 0.08, 0.060, 0.062, 0.3, 'summer']
bacteria = [1000, 0.12, 0.08, 0.06, 0.06, 0.3, 'twilight']
cheetah = [400, 0.08, 0.08, 0.06, 0.06, 0.3, 'copper']
squid = [10000, 0.16, 0.08, 0.06, 0.062, 0.3, 'pink']
reptile = [10000, 0.14, 0.06, 0.035, 0.065, 0.2, 'gist_earth']
peacock = [1000, 0.1, 0.2, 0.06, 0.07, 0.2, 'ocean']

# example with cheetah pattern
pattern = cheetah
A, B = initial_conditions(s=400, a=0.50, b=0.25, r=pattern[5])

# animate pattern evolution
animate(n=pattern[0], A=A, B=B, DA=pattern[1], DB=pattern[2], f=pattern[3], k=pattern[4], color=pattern[6])

# plot final pattern
plot(n=pattern[0], A=A, B=B, DA=pattern[1], DB=pattern[2], f=pattern[3], k=pattern[4], color=pattern[6])
