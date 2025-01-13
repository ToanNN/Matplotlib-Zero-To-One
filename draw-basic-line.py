import matplotlib.pyplot as plt

# Create a figure and a single subplot (axes) - graph
fig, ax = plt.subplots()

# Plot data on the graph here x[i] will matched with y[i]
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
ax.plot(x, y, label='quadratic', color='b')

# Add labels and title and legends
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Example Plot')
ax.legend()

# Display the plot
plt.show()

## Math expressions in text
# Matplotlib accepts TeX equation expressions in any text expression
ax.set_title(r'$\sigma_i=15$')
#where the r preceding the title string signifies that the string is a raw string and not to treat backslashes as python escapes.


