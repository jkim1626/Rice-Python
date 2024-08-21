### PROBLEM 1 (Markov Chain)

"""
The "Problem"
Your friend goes to a nearby university (not Rice!) with a terrible dining hall.  
The chef knows how to make only three things: chicken nuggets (C), spaghetti (S), and tacos (T).  
Further, the menu is not announced in advance, so your friend never knows what's going to be available on any given day. 
Over the past few weeks, the following sequence of dishes have been served for dinner:

C, C, S, T, S, T, C, S, S, T, C, S, C, C, T, S, T, S, S, C, T

Your friend doesn't like tacos, so he'd like you to figure out how to predict when tacos will be 
served so that your friend can make other plans on those days.

Python
Write a Python program to build the 0th order Markov chain.  
Run it on the dinner fare data above.  
Your function should take a list as input and return a dictionary whose keys are the possible states and 
where the value associated with each key is the probability associated with the corresponding new state, based on that input.  
Check that the probabilities match what you computed by hand.

Your function should run on any list of data, not just those that contain the three letters C, S, and T.

To test your function, write another function that returns a list of random numbers (using random.randrange). 
This function should be able to generate a list of any given length, generating random numbers over any given interval.

Use this function to generate some lists of random numbers, and for each list, then print that list and the corresponding 0th order Markov chain model.  
Confirm by hand that the results are correct.  
The states here will be the individual numbers in the generated list, rather than the letters as used in the dining hall example above.
"""

from collections import defaultdict

def zero_markov(items):
    prob = defaultdict(float)
    for item in items:
        prob[item] += 1
    
    for key in prob:
        prob[key] /= len(items)
        
    return prob

# Given sequence of dishes
dishes = ['C', 'C', 'S', 'T', 'S', 'T', 'C', 'S', 'S', 'T', 'C', 'S', 'C', 'C', 'T', 'S', 'T', 'S', 'S', 'C', 'T']

# Compute the 0th order Markov chain for the dishes
print(zero_markov(dishes))

import random

def generate_random_list(length, interval):
    return [random.randrange(interval[0], interval[1] + 1) for _ in range(length)]

# Generate a random list of 10 numbers between 1 and 5
random_list = generate_random_list(10, (1, 5))

# Compute the 0th order Markov chain for the random list
print(random_list)
print(zero_markov(random_list))
