import matplotlib.pyplot as plt

# Creating a figure
fig, ax = plt.subplots(figsize=(10, 0.5))

# Plotting a horizontal line for x-axis
ax.axhline(y=0, color='black')

# Setting x-axis scale to log
ax.set_xscale('log')

# Setting labels and title
ax.set_xlabel('Conductivity')
ax.set_title('Conductivity of Polymers')

# Removing y-axis
ax.get_yaxis().set_visible(False)

# Setting x-axis limits
ax.set_xlim(1e-16, 1e8)

# Adjusting the x-axis tick intervals to increase by 10^2
ax.set_xticks([10**i for i in range(-16, 9, 2)])

# Adjusting plot margins
plt.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1)

# Showing the plot
plt.show()
