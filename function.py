# Plot Title
title = 'Interpolation of Runge function'

# Function's name
name_f = 'runge'

# Initial x value
start = -1

# Final x value
end = 1

# Min node amount
k = 2

# Max node amount
n = 31

# Linspace
m = 201

# Function
def f(x):
    return 1 / (1 + 25*x**2)