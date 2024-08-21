import simpleplot
import math

def hill_descent(fxn, initial_pos, step_size):
    """
    Find a local minimum of fxn, beginning the search
    at initial_pos and moving step_size either left
    or right during each iteration.

    Inputs:
      fxn         -- a function that takes a number as
                     an argument and returns a number
      initial_pos -- position to start evaluating fxn at
      step_size   -- step size to use in hill descent 
                     process

    Returns:
      The location of the local minimum found via hill
      descent using the given initial position and step
      size.
    """
    minimum = fxn(initial_pos)
    current_pos = initial_pos
    left_test = fxn(initial_pos - step_size)
    right_test = fxn(initial_pos + step_size)
    
    while minimum > left_test or minimum > right_test:
        if right_test > left_test:
            right_test = minimum
            minimum = left_test
            current_pos = current_pos - step_size
            left_test = fxn(current_pos)
        else:
            left_test = minimum
            minimum = right_test
            current_pos = current_pos + step_size
            right_test = fxn(currrent_pos)
    return current_pos

def fxn(x):
    return (x ** 2) - (6 * x) + 11

def gxn(x):
    return (x ** 6) - 31*(x ** 5) + 369*(x ** 4) - 2072*(x ** 3) + 5595*(x ** 2) - 6300 * x + 3000 

def hxn(x):
    return (math.cos(x) + 2) / (x ** 2 + 20)



print(hill_descent(fxn, 3, 1))
print(hill_descent(gxn, 10, 1))
print(hill_descent(hxn, 10, 1))

def plot(name, fxn, xstart, xend):
    """
    Plot the input function between xstart and xend.

    Inputs:
      name   -- String name of the function for
                the title of the plot
      fxn    -- a function that takes a number as
                an argument and returns a number
      xstart -- starting value for the plot
      xend   -- ending value for the plot

    Returns:
      None
    """    
    # Evaluate the function at 100 points in the specified range.
    vals = []
    delta = (xend - xstart) / 100.0
    for num in range(100):
        xval = xstart + num * delta
        vals.append((xval, fxn(xval)))
        
    # Plot the function at those 100 points
    simpleplot.plot_lines('Function ' + name, 400, 300, 'x', 'f(x)', [vals], False)
    
    
print(plot("1", fxn, 0, 10))
print(plot("2", gxn, 0, 10))
print(plot("3", hxn, 0, 10))
