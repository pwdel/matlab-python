# Import numpy to be able to do math stuff
import numpy as np
# Import matplotlib to be able to plot stuff
import matplotlib
import matplotlib.pyplot as plt, mpld3


# Create an array of 100 random numbers with values 0 to 1
Y = np.random.rand(100)

# Create an array of numbers 1 to 100 - note it's "arange" not "arrange"
X = np.arange(100)

# Plot with formatting
plt.plot(X,Y, 'ks-', mec='w', mew=5, ms=10)
# Display in a web browser
mpld3.show()

exit()
