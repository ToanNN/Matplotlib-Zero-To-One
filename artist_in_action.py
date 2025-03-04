import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np

fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(211)
ax1.set_ylabel('Voltage [V]')
ax1.set_title('A sine wave')

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax1.plot(t, s, color='blue', lw=2)

# Fixing random state for reproducibility
np.random.seed(19680801)

ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
n, bins, patches = ax2.hist(np.random.randn(1000), 50,
                            facecolor='yellow', edgecolor='yellow')
ax2.set_xlabel('Time [s]')

l1 = lines.Line2D([0,1], [1,1], transform = fig.transFigure, figure = fig)
l2 = lines.Line2D([1,1], [3,4], transform = fig.transFigure, figure = fig)
fig.lines.extend([l1, l2])

plt.show()