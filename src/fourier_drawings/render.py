from math import sin, cos, pi

import matplotlib
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.text import Annotation
import numpy as np

from fourier_drawings.utils import format, render_circle, calculate_for_n_circles, render_arrow

matplotlib.rcParams['axes.edgecolor'] = '#ffffff'


fig, ax = plt.subplots()
format(fig, ax, 4)


start = 0
end = 2*pi*10
step = 0.01


rng = np.linspace(start, end, num=int(end//step))

x: list[float] = [cos(v) for v in rng]
y: list[float] = [sin(v) for v in rng]

times = np.linspace(start, end, int(end/step))

def render(
        ws: list[float],
        ph0s: list[float],
        ls: list[float],
        speed: float = 20
        ) -> None:
    x: list[float] = []
    y: list[float] = []

    # map the figure itself

    for i in times:
        xy: tuple[float, float] = calculate_for_n_circles(i, ws, ph0s, ls)[-1]
        x.append(xy[0])
        y.append(xy[1])

    # start plotting
    pl, = ax.plot(x, y, zorder=0) # type: ignore
    pl.set_xdata([])
    pl.set_ydata([])

    prev_arrows: list[Annotation] = []
    prev_circles: list[Patch] = []

    def update(frame: int) -> list[Line2D]:
        # clean up after prev frame
        for arrow in prev_arrows:
            arrow.remove()
        for circle in prev_circles:
            circle.remove()

        prev_circles.clear()
        prev_arrows.clear()


        # get new circle centres
        t = times[frame]
        cords: list[tuple[float, float]] = calculate_for_n_circles(t, ws, ph0s, ls)

        if frame != int(end//step)-1:
            ## draw circles
            for i in range(len(cords)-1):
                xi, yi = cords[i]
                prev_circles.append(render_circle(ax, xi, yi, ls[i]))

            ## draw arrows: each begins at center of circle n and ends at center of circle n+1
            for i in range(len(cords)-1):
                x0, y0 = cords[i]
                x1, y1 = cords[i+1]
                prev_arrows.append(
                    render_arrow(ax, (x0, y0), (x1, y1))
                )

        # update the figure
        pl.set_xdata(x[:frame])
        pl.set_ydata(y[:frame])

        return [pl]

    plt.get_current_fig_manager().full_screen_toggle() #type: ignore

    ani = animation.FuncAnimation(fig, update, frames=int(end//step), interval=speed, repeat=False) #type: ignore

    plt.show() #type: ignore
