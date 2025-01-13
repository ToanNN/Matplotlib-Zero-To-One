import matplotlib.pyplot as plt
import numpy as np

## OOP Style
x = np.linspace(0, 10, 1)


figure, axes= plt.subplots(figsize=(5, 2.7), layout='constrained')
axes.plot(x, x, label= 'linear', color ='r')
axes.plot(x, x**2 + 9, label='quadratic + 9', color ='blue')
axes.plot(x, x**3, label='cubic')  # ... and some more.

axes.set_xlabel('x value')
axes.set_ylabel('y value')
axes.set_title(r'$\sigma_i=15$')
axes.legend() # Add legends to the figure

plt.show()

