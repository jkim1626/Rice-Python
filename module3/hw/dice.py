### PROBLEM 1 (ROLLING DICE)

"""
First you should write a function roll(ndice, nsides).
he first parameter, ndice, is the number of dice to roll,
which must be greater than or equal to 1.
The second parameter, nsides, is the number of sides on each die 
(assume all of the dice you are rolling have the same number of sides),
which also must be greater than or equal to 1.
Your function should return the sum of all of the dice that were rolled.

Now, you are going to roll the dice and plot the results. 
The objective of your experiments is to determine the distribution of the results of rolling dice. 
Design and run several experiments and use simpleplot to plot the results.  
"""

import random as rand

def roll_dice(ndice, nsides):
    dice = []
    for i in range(ndice):
        temp = rand.randint(1, nsides)
        dice.append(temp)
    
    print(dice)
    sum = 0
    for j in range(ndice):
        sum += dice[j]
    
    return sum

print(roll_dice(3,6))









from collections import defaultdict
import simpleplot

def test(num_rolls, ndice, nsides):
    '''
    Objective: to plot the distribution of dice rolls executed by roll
    Input: num_rolls ← integer representing number of times roll should be executed, number of points plotted, 
           ndice ← an integer representing the number of dice we are rolling, 
           nsides ← the number of sides on each dice
    Output: graph ← a bar graph representing the distribution of the sum of dice rolls
    '''
    dataset = defaultdict(int)
    while num_rolls > 0:
        new_point = roll_dice(ndice, nsides)
        dataset[new_point] += 1
        num_rolls -= 1
        
    graph = simpleplot.plot_bars("dice roll distribution", 400, 600, "sum", "distribution", [dataset])
    return graph


#increasing number of tests for the same ndice and nsides
#print(test(10,3,6))
#print(test(100,3,6))
#print(test(1000,3,6))

#lower number of 
# print(test(1000,1,1))
# print(test(1000,2,2))
# print(test(1000,3,3))
# print(test(100000,1,6))