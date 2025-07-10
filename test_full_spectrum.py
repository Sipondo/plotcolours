# From: https://matplotlib.org/stable/gallery/color/color_cycle_default.html

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from matplotlib.colors import TABLEAU_COLORS, same_color


def show_cycle(name='default'):
    def f(x, a):
        """A nice sigmoid-like parametrized curve, ending approximately at *a*."""
        return 0.85 * a * (1 / (1 + np.exp(-x)) + 0.2)


    fig, ax = plt.subplots()
    ax.axis('off')
    ax.set_title(f"Colors in the {name} property cycle")

    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']
    x = np.linspace(-4, 4, 10)

    for i, (color, color_name) in enumerate(zip(colors, colors)):
        assert same_color(color, color_name)
        pos = 4.5 - i
        ax.plot(x, f(x, pos))
        ax.text(4.2, pos, f"'C{i}': '{color_name}'", color=color, va="center")
        ax.bar(9, 1, width=1.5, bottom=pos-0.5)

    plt.savefig(f'results/spectrum_{name}.png')
    plt.show()

show_cycle("default")
import plotcolours
show_cycle("plotcolours")

# Save grayscale versions of the generated PNGs
for fname in ['results/spectrum_default.png', 'results/spectrum_plotcolours.png']:
    img = Image.open(fname).convert('L')
    gray_fname = fname.replace('.png', '_grayscale.png')
    img.save(gray_fname)
