import matplotlib.pyplot as plt
import numpy as np

# The Figure is the final image, and may contain one or more Axes.

# The Axes represents an individual plot (not to be confused with
# Axis, which refers to the x-, y-, or z-axis of a plot).


data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}

group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

# the figsize keyword argument follows the form (width, height) inches.
fig, ax = plt.subplots(figsize =(8,8))

# make rooms for elements in the plot
plt.rcParams.update({'figure.autolayout': True})

print(plt.style.available)

# Activate a style
plt.style.use('fivethirtyeight')

# Draw a horizontal bar chart
ax.barh(group_names, group_data)

labels = ax.get_xticklabels()
# Set properties of many items at once, we can use setp
# Set the properties of labels
plt.setp(labels, rotation = 45, horizontalalignment='right')


# add labels to the plot
ax.set(xlim=[-10000, 140000], xlabel = 'Total Revenue', ylabel='Company',title='Company Revenue')

# Define custom formatter for x axis
def currency(x, pos):
    """The two arguments are the value and tick position"""
    if x >= 1e6:
        s = f'${x*1e-6:1.1f}M'
    else:
        s = f'${x*1e-3:1.0f}K'
    return s
ax.xaxis.set_major_formatter(currency)
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])


# Draw another vertical line for the mean
ax.axvline(group_mean, ls ='--', color='r')

# Annotate new companies

for group in [2,5,8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment='center')
# Now we move our title up since it's getting a little cramped
ax.title.set(y=1.05)

# Save out plot
print(fig.canvas.get_supported_filetypes())
plt.show()