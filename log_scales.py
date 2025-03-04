import matplotlib.pyplot as plt
import numpy as np

# Axes are the coordinate system
# Fixing random state for reproducibility
np.random.seed(19680801)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)

y = y[(y >0) & (y<1)]
y.sort()
x= np.arange(len(y))

# Plot with various axes scales
plt.figure()

# linear
# Create a 2x2 grid and selects the first subplot
plt.subplot(221)
plt.plot(x,y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# Log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log at the 3rd subplot
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog')
plt.grid(True)

# logit at the fourth subplot
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.1, right=0.95, hspace=0.25, wspace=0.35)

plt.show()