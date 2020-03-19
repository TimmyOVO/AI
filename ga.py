import matplotlib.pyplot as plt
import numpy


# 求解the_function在[0,15]的最大值

# Generate some individual with random genetic
# Calculate individual's fitness and pick some individual
# Crossover their genetic using specific rule(s)
# Make their child mutation
# Repeat step 1 until result meet the stop conditions

def the_function(z):
    return z + 10 * numpy.sin(5 * z) + 7 * numpy.cos(4 * z)


x = numpy.linspace(0, 15)
y = the_function(x)
plt.plot(x, y)
plt.show()
