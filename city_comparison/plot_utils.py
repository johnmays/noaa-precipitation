from matplotlib import cm, colors
import numpy as np

_N = int(256/0.8)
_Blues = cm.get_cmap('Blues', _N)
_subsection_colors = _Blues(np.linspace(0, 1, _N))
_subsection_colors = _subsection_colors[(_N-256):_N, :]
Blues_subsection = colors.ListedColormap(_subsection_colors)