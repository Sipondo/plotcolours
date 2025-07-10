from cycler import cycler
import matplotlib as mpl
import matplotlib.pyplot as plt

# Distinguishable colours (hex codes) - 12 colours
# Ordered for maximum distinguishability, especially in greyscale
dist_colours = [
    "#0070DE",  # Blue (dark)
    "#ABD473",  # Green (medium)
    "#9482C9",  # Violet (medium)
    "#C41F3B",  # Red (dark)
    "#00FF96",  # Teal/Green (light)
    "#A330C9",  # Purple (dark)
    "#F58CBA",  # Pink (light)
    "#FF7D0A",  # Orange (medium)
    "#C79C6E",  # Brown (medium)
    "#FF4D6B",  # Magenta/Red (bright)
    "#69CCF0",  # Light blue (light)
    "#FFD100",  # Yellow (very light)
]
# Define distinguishable marker patterns and linestyles
dist_markers = ['o', 's', 'D', '^', 'v', '>', '<', 'P', 'X', '*', 'h', '+']

# Define distinguishable hatching patterns for histograms
dist_hatches = [
    '/',    # 1
    '\\',   # 2
    '|',    # 3
    '-',    # 4
    '+',    # 5
    'x',    # 6
    'o',    # 7
    'O',    # 8
    '.',    # 9
    '*',    # 10
    '//',   # 11
    '\\\\', # 12
]

# Linestyles for better greyscale distinction
dist_linestyles = [
    '-',                # 1
    '--',               # 2
    '-.',               # 3
    ':',                # 4
    (0, (3, 1, 1, 1)),  # 5
    (0, (5, 5)),        # 6
    (0, (1, 1)),        # 7
    (0, (3, 5, 1, 5)),  # 8
    (0, (5, 1)),        # 9
    (0, (2, 2)),        # 10
    (0, (3, 1, 1, 1, 1, 1)), # 11
    (0, (1, 1, 10, 1))  # 12
]

# Set global rcParams for matplotlib to use the custom styles by default

mpl.rcParams['axes.prop_cycle'] = (cycler('color', dist_colours) + 
                                  cycler('marker', dist_markers) + 
                                  cycler('linestyle', dist_linestyles))
mpl.rcParams['lines.marker'] = 'o'  # Default marker (will be cycled)
mpl.rcParams['lines.linestyle'] = '-'  # Default linestyle (will be cycled)
mpl.rcParams['patch.edgecolor'] = 'black'  # For bar/histogram edges
mpl.rcParams["patch.force_edgecolor"] = True


# Monkeypatch plt.bar to automatically hatch bars with distinguishable patterns
_original_bar = plt.bar

def hatched_bar(*args, **kwargs):
    bars = _original_bar(*args, **kwargs)
    # Apply hatches in a cycle
    for i, bar in enumerate(bars):
        hatch = dist_hatches[i % len(dist_hatches)]
        bar.set_hatch(hatch)
    return bars
plt.bar = hatched_bar

# Monkeypatch plt.hist to automatically hatch histogram patches with distinguishable patterns
_original_hist = plt.hist
_hist_hatch_offset = 0

def hatched_hist(*args, **kwargs):
    global _hist_hatch_offset
    kwargs["hatch"] = dist_hatches[_hist_hatch_offset]
    _hist_hatch_offset = (_hist_hatch_offset + 1) % len(dist_hatches)
    n, bins, patches = _original_hist(*args, **kwargs)
    return n, bins, patches

plt.hist = hatched_hist
