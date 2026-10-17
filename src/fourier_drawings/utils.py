from math import sin, cos

from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.text import Annotation


def format(fig: Figure, ax: Axes, box_size: int = 0) -> None:

    ax.tick_params(axis='x', colors='#ffffff') #type: ignore
    ax.tick_params(axis='y', colors='#ffffff') #type: ignore

    ax.set_aspect('equal', 'box')
    if box_size:
        ax.set_xlim(-box_size, box_size)
        ax.set_ylim(-box_size, box_size)

    ax.set_facecolor('#111117')
    fig.set_facecolor('#111117')


def project_point(
        t: float,
        x0: int | float,
        y0: int | float,
        omega: float,
        l: float = 1,
        ph0: float = 0
        ) -> tuple[float, float]:
    return x0 + l * cos(omega*t + ph0), y0 + l * sin(omega*t + ph0)


def render_circle(
        ax: Axes,
        x0: float,
        y0: float,
        l: float
    ):
    return ax.add_patch(plt.Circle((x0, y0), l, fill=False, color='w')) #type: ignore


def calculate_for_n_circles(
        t: float,
        omegas: list[float],
        ph0s: list[float],
        ls: list[float]
    ) -> list[tuple[float, float]]:
    assert len(omegas) == len(ph0s)
    assert len(ph0s) == len(ls)


    cords: list[tuple[float, float]] = [(0.0, 0.0)]

    for i in range(1, len(ls)+1):
        x_i, y_i = project_point(
            t,
            cords[i-1][0],
            cords[i-1][1],
            omegas[i-1],
            ls[i-1],
            ph0s[i-1]
            )

        cords.append((x_i, y_i))

    assert len(cords) == len(ls) + 1

    return cords


def render_arrow(ax: Axes, begin: tuple[float, float], end: tuple[float, float]) -> Annotation:
    return ax.annotate('', xytext=begin, xy=end, arrowprops=dict(arrowstyle='->', color='w')) #type: ignore
