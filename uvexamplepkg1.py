from math import tau

import numpy as np


def create_circle(
    N: int, r: float = 1.
) -> np.ndarray[tuple[int, int], np.dtype[np.float64]]:
    """
    Creates an numpy ndarray which represents a circle of radius `r`.
    The first column is x and the 2nd column is y.

    Parameters
    ----------
    r : float
        Radius of the circle to create.

    N : int
        Number of points in the circle

    """

    t = np.linspace(0, tau, num=N)
    circle = np.empty((N, 2))
    circle[:, 0] = r * np.cos(t)
    circle[:, 1] = r * np.sin(t)

    return circle


# Optional features
try:
    import matplotlib.pyplot as plt

    def plot_circle(N: int, r: float = 1.):
        """
        Generates and plots a circle with radius `r` with `N` data points.

        Parameters
        ----------
        r : float
            Radius of the circle to create.

        N : int
            Number of points in the circle

        """

        _ = plt.plot(*create_circle(N, r).T)
        plt.show()

except ImportError:
    pass

plot_circle(10)  # type: ignore
