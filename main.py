import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = 100*[0], 100*[0]
# Your code goes here



# This will draw the graph
plt.plot( xdata, ydata, 'bo')
plt.plot( [0,1], [1,2], 'k-' )
plt.plot( [0,1], [3,4], 'k-' )
plt.savefig("correlated_variables.png")
