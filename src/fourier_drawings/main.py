from math import atan2, cos, pi, sin, sqrt

import numpy as np

from fourier_drawings.render import render
from svg_parce import dots


def integrate(n: int) -> tuple[float, float]:
    dt = 2*pi/len(dots)

    x = 0
    y = 0

    k = 0
    while k < len(dots):
        xi, yi = dots[k]
        angle: float = k*dt*n

        x_turned = xi * cos(angle) + yi * sin(angle)
        y_turned = yi * cos(angle) - xi * sin(angle)

        x += x_turned*dt
        y += y_turned*dt

        k += 1

    y *= 1/(2*pi)
    x *= 1/(2*pi)

    ph0 = atan2(y, x)
    l = sqrt(x**2 + y**2)

    return ph0, l


def fourier(k: int):
    phases: list[float] = []
    ls: list[float] = []
    ws: list[int] = []

    for n in range(-k, k+1):
        ph0, l = integrate(n)
        phases.append(ph0)
        ls.append(l)
        ws.append(n)

    render(ws, phases, ls) #type: ignore

fourier(150)
