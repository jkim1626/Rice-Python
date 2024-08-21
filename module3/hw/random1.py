### PROBLEM 1
"""
It is possible to estimate the value of pi simply by picking random numbers. 
The key insight is that you can do this by picking pairs of random numbers that represent the 
(x,y) coordinate inside of a unit square with its lower left corner at the origin:
"""

import random as rand

pi = 3.14159265

def estimate_pi(n):
    # Initialize a counter variable to count "successful" hits
    count = 0
    
    # Loop through the number of iterations and create a x and y point for each
    # Given the area of a unit circle is x^2 + y^2 = 1
    # We can write a loop that checks if the square of each pair of coordinates is <= 1
    for i in range(n):
        x_val = rand.uniform(0,1)
        y_val = rand.uniform(0,1)
        if (x_val**2 + y_val**2 <= 1):
            count += 1
            
    # Statistically, the count / n should return an estimate for pi/4
    return 4 * (count / n)
    
"""
print(pi)
print(estimate_pi(10))
print(estimate_pi(100))
print(estimate_pi(1000))
print(estimate_pi(10000))
print(estimate_pi(100000))
print(estimate_pi(1000000))
"""    






### PROBLEM 2
"""
It is often very useful when you have a collection of numbers to create a histogram of those numbers. 
Write a Python function that takes a list of numbers as inputs and returns a dictionary that has the numbers 
in the list as keys and the number of times the number appears as values.

For example, given the input [1, 1, 2, 1, 3, 1, 2, 2, 4], your function should return {1: 4, 2: 3, 3: 1, 4: 1}. 
Once you have such a dictionary, you could easily plot it as a histogram. We will learn how to do that in future lectures.
"""
import random as rand

def histogram(list):
    # Define an empty dictionary
    dictionary = {}
    
    # Define a list for seen integer values
    seen = []
    
    # Iterate through all of the elements in the list
    for i in range(len(list)):
        # If the element is new (not in seen), 
        # then add it to the seen list and initialize a dictionary key 
        # Otherwise do not change seen list and instead increment dictionary value
        if list[i] not in seen:
            seen.append(list[i])
            dictionary[list[i]] = 1        
        else:
            dictionary[list[i]] += 1
        
    return dictionary

def check_histogram(dict, list):
    # Iterate through the original list and decrement dictionary values for each element 
    for i in range(len(list)):
        if list[i] in dict:
            dict[list[i]] -= 1
            
    # If the dictionary has any values != 0, then return false
    for l in range(len(dict)):
        if dict[list[i]] != 0:
            return False
            
    return True
        

# Create a list of integer values in range [0,5]
list = []
for i in range(10):
    x = rand.randint(0,5)
    list.append(x)

"""
print(list)
print(histogram(list))
print(check_histogram(histogram(list), list))
"""







### PROBLEM 3
"""
Sometimes you would like to choose among a set of options equally. 
Other times, you would like different options to have different probabilities of being selected (a weighted random choice).
For example, if you wanted to pick random numbers with the same frequency as they occurred in some input, 
you would use the frequency of occurrence in the input as the probability distribution for the selection.

Write a function that takes a dictionary as input and randomly selects one of the keys of the dictionary. 
The values in the dictionary should be the probability of selecting the associated key.
If you repeatedly call the function enough times, the distribution of the output should look identical to the input.
"""

import random as rand

# Function to create a histogram from a list
def histogram(list_1):
    dictionary = {}
    seen = []
    
    for i in range(len(list_1)):
        if list_1[i] not in seen:
            seen.append(list_1[i])
            dictionary[list_1[i]] = 1        
        else:
            dictionary[list_1[i]] += 1
        
    return dictionary
    
# Function to calculate probabilities from a histogram
def probabilities(hist_dict):
    # Get the total sum of occurrences of each integer in the histogram
    total_sum = 0
    for x in hist_dict:
        total_sum += hist_dict[x]
    
    # Change the value of each key to the probability of that key being picked
    for x in hist_dict:
        temp = round(hist_dict[x] / total_sum, 3)
        hist_dict[x] = temp
    
    return hist_dict
    
# Function to make a weighted choice based on probabilities
def weighted_choice(hist_dict):
    hist_dict = probabilities(hist_dict)
    
    # Create a list with 100 values corresponding to the probability distribution of keys
    list_2 = []
    for key in hist_dict:
        temp = hist_dict[key] * 100
        for i in range(int(temp)):
            list_2.append(key)
    
    rand_num = rand.randint(0,99)
    
    return list_2[rand_num]

"""
# Generate a list with random numbers
list_3 = []
for i in range(10):
    x = rand.randint(0,5)
    list_3.append(x)

# Test to see if looping this function over n iterations mirrors the distribution
n = 1000
list_4 = []
for i in range(n):
    temp = weighted_choice(histogram(list_3))
    list_4.append(temp)

# Calculate probabilities for the original and new lists
dict1 = probabilities(histogram(list_3))
dict2 = probabilities(histogram(list_4))

# Print the sorted dictionaries
print(dict1)
print(dict2)
"""