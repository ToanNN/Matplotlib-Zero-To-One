import matplotlib.pyplot as plt

# If you provide a single list or array to plot, matplotlib assumes it is a sequence of y values, 
# and automatically generates the x values for you.
# Since python ranges start with 0, the default x vector has the same length as y but starts with 0; therefore, the x data are [0, 1, 2, 3].
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')

# Define the points and drawn as red circles
plt.plot([1,2,3,5], [1,4,9,25], 'ro')

# Define the axis range [xmin, xmax, ymin, ymax]
plt.axis((0,10, 0, 100))
plt.show()

# Draw several lines
import numpy as np
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


## Draw a dataframe 

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

# Accessing data by property names
plt.scatter('a', 'b', data = data)

plt.show()