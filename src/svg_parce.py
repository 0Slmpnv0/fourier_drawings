from svgpathtools import svg2paths #type: ignore
import numpy as np

paths, attributes = svg2paths('initial_line/fourier.svg') #type: ignore


dots: list[tuple[float, float]] = []

step = 0.001
for p in paths:
    for i in np.linspace(0, 1, int(1/step)):
        dots.append((p.point(i).real, -p.point(i).imag)) #type: ignore

cx = sum(x for x, _ in dots) / len(dots)
cy = sum(y for _, y in dots) / len(dots)
dots = [(x - cx, y - cy) for x, y in dots]
