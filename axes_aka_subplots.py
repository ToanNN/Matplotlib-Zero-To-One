import matplotlib.pyplot as plt
import numpy as np

fg, axs = plt.subplots(ncols=2, nrows=2, figsize =(6,6),
                       layout='constrained')

# for each axes add a label in the middle
for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'Axes[{row},{col}]', (0.5, 0.5),
                               transform = axs[row, col].transAxes,
                               ha='center', va='center', fontsize=18,
                               color='darkgrey')
fg.suptitle('Subplots in Columns and Rows')

plt.show()

