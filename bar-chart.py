import matplotlib.pyplot as plt
import numpy as np

# Create 1 row two columns and get each graph to draw on
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (5,3), layout='constrained')

# draw a bar chart on the first plot
categories = ['cuti', 'thi met', 'thang cu', 'con him']
ax1.bar(categories, np.random.rand(len(categories)))

# draw a line chart on the second plot
ax2.plot([1,2,3], [8,15,6])
# Display the plot
plt.show()

# Or we can access the plot by indexes

from matplotlib.colors import LogNorm

X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

fig, axs = plt.subplots(2, 2, layout='constrained')
pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0, 0])
axs[0, 0].set_title('pcolormesh()')

co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
fig.colorbar(co, ax=axs[0, 1])
axs[0, 1].set_title('contourf()')

pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma', norm=LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=axs[1, 0], extend='both')
axs[1, 0].set_title('imshow() with LogNorm()')


fig.colorbar(pc, ax=axs[1, 1], extend='both')
axs[1, 1].set_title('scatter()')