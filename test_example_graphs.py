import numpy as np
from cycler import cycler
import matplotlib as mpl

import matplotlib.pyplot as plt

import plotcolours
from PIL import Image

STYLES_TO_TEST = 12

x = np.linspace(-10, 10, 10)
plt.figure(figsize=(10, 6))

for i in range(STYLES_TO_TEST):
    y = (x + i) ** 2
    plt.plot(x, y, label=f'Line {i+1}')

plt.legend()
plt.title('Line Test with Distinguishable Parabolas')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('results/line_test.png')
plt.show()


# Overlapping histogram test
plt.figure(figsize=(10, 6))
data = [np.random.normal(loc=i*2, scale=2, size=100) for i in range(STYLES_TO_TEST)]
for i, d in enumerate(data):
    plt.hist(d, bins=20, alpha=0.7, label=f'Style {i+1}')
plt.legend()
plt.title('Histogram Test with Distinguishable Colours and Hatches')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.savefig('results/histogram_test.png')
plt.show()


# Barplot test
plt.figure(figsize=(10, 6))
bar_heights = np.arange(1, STYLES_TO_TEST + 1)
bars = plt.bar(
    np.arange(STYLES_TO_TEST),
    bar_heights,
)

# Use the default color cycle from rcParams for bar colors
default_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
bar_colors = [default_colors[i % len(default_colors)] for i in range(STYLES_TO_TEST)]
bars = plt.bar(
    np.arange(STYLES_TO_TEST),
    bar_heights,
    color=bar_colors
)
plt.xticks(np.arange(STYLES_TO_TEST), [f'Style {i+1}' for i in range(STYLES_TO_TEST)], rotation=45)
plt.title('Barplot Test with Distinguishable Colours and Hatches')
plt.xlabel('Class')
plt.ylabel('Value')
plt.tight_layout()

plt.savefig('results/barplot_test.png')
plt.show()

# Save grayscale versions of the generated PNGs
for fname in ['results/line_test.png', 'results/histogram_test.png', 'results/barplot_test.png']:
    img = Image.open(fname).convert('L')
    gray_fname = fname.replace('.png', '_grayscale.png')
    img.save(gray_fname)
