from svgpathtools import svg2paths #type: ignore
import numpy as np

paths, attributes = svg2paths('initial_line/fourier.svg') #type: ignore


dots: list[tuple[float, float]] = []

step = 0.01
for p in paths:
    for i in np.linspace(0, 1, int(1/step)):
        dots.append((p.point(i).real, p.point(i).imag)) #type: ignore

print(dots)
