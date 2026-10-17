# Fourier Drawings

Draw shapes with epicycles. A chain of rotating circles (a Fourier series of
vectors) is summed tip-to-tip, and the path traced by the final tip reproduces
an input curve. The result is animated with matplotlib: each circle and its
arrow is drawn every frame while the traced curve grows behind them.

## How it works

- **`src/svg_parce.py`** samples points along the paths of an SVG file
  (`initial_line/fourier.svg`) and turns them into a list of `(x, y)`
  coordinates — the target curve to approximate.
- **`src/fourier_drawings/utils.py`** holds the math and drawing helpers:
  projecting a point for a rotating vector (`project_point`), summing `n`
  circles into a chain of centres (`calculate_for_n_circles`), and rendering
  circles and arrows onto the axes.
- **`src/fourier_drawings/render.py`** builds the matplotlib figure and runs the
  animation. Given per-circle angular frequencies (`ws`), phase offsets
  (`ph0s`) and radii (`ls`), it animates the epicycle chain and draws the curve
  its tip traces.

## Requirements

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/) (recommended) for dependency management

Dependencies: `matplotlib`, `numpy`, `svgpathtools`.

## Setup

```bash
uv sync
```

## Usage

Sample points from the bundled SVG:

```bash
uv run python src/svg_parce.py
```

To render an animation, call `render(ws, ph0s, ls)` from
`fourier_drawings.render` with the frequencies, phases and radii of the circles
you want to chain together.
