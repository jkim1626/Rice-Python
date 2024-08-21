# ********************************* Spot it! and Lists *********************************

# 1) Write a function, middle, that takes a list of numbers as 
#    input and returns the number in the middle of the list.

import math

def middle(list):
    size = len(list)
    if size % 2 == 0:
        middle2 = int(size / 2)
        middle1 = int((size / 2) - 1)
        print("The middle two numbers are", list[middle1], "and", list[middle2])
    else:
        middle = math.trunc(size / 2)
        print("The middle number is", list[middle])
        
"""    
list = [1,2,3,4,5,6,7]
middle(list)
               
second_list = [1,2,3,4,5,6,7,8]
middle(second_list)
"""

# 2) Write a function that is a variation of the somewhat famous 
#    (and undeniably stupid) "fizzbuzz" interview screening 
#    question.  Your function should take a number as input and 
#    print it, unless the number is divisible by 3 or 5.  If it 
#    is divisible by 3, print "fizz".  If it is divisible by 5, 
#    print "buzz".  If it is divisible by both, print "fizzbuzz".

# Method 1
def output():
    for int in range(1, 101):
        if (int % 3 == 0) and (int % 5 == 0):
            print("fuzzball")
        elif int % 3 == 0:
            print("fuzz")
        elif int % 5 == 0:
            print("ball")
        else:
            print(int)

# Method 2            
def output():
    for int in range(1, 101):
        string = ""
        if (int % 3 == 0) and (int % 5 == 0):
            string += "fuzzball"
        elif int % 3 == 0:
            string += "fuzz"
        elif int % 5 == 0:
            string += "ball"
        else:
            string += str(int)
        print(string)

"""
output()
"""
 
# 3) Write a function, rotate_left, that takes a list as input 
#    and rotates the list to the left.  
#
#    For example, the result for rotate_left([1, 2, 3]) should
#    be [2, 3, 1].

# Method 1 (Only works for shift of 1
def rotate_left(list):
    list_rotated = []
    # Create a copy of list onto list_rotated
    for i in range(len(list)):
        list_rotated.append(list[i])
    print("Original:",list_rotated)
    
    for i in range(len(list) - 1):
        list_rotated[i] = list[i + 1]
    list_rotated[len(list) - 1] = list[0]
    print("Rotated: ", list_rotated)
        
# Method 2 (Works for n rotations
def rotate_left2(lst, n):
    if not lst:
        return lst
    
    n = n % len(lst)  
    return lst[n:] + lst[:n]

"""
list = [1,2,3,4,5]    
rotate_left(list)

list = [1,2,3,4,5]    
print(rotate_left1(list, 3))
"""

# 4) Write a function, rotate_right, that takes a list as input
#    and rotates the list to the right.
#
#    For example, the result for rotate_right([1, 2, 3]) should
#    be [3, 1, 2].

# Method 1 (Only works for rotation of 1)
def rotate_right(list):
    list_rotated = []
    # Create a copy of list onto list_rotated
    for i in range(len(list)):
        list_rotated.append(list[i])
    print("Original:",list_rotated)
    
    list_rotated[0] = list[len(list) - 1]
    for i in range(len(list)):
        list_rotated[i] = list[i - 1]
    print("Rotated: ", list_rotated)

# Method 2 (Works for n rotations)
def rotate_right2(list,n):
    if not list:
        return list
    
    n = n % len(list)
    return list[-n:] + list[:-n] 

"""
list = [1,2,3,4,5]
rotate_right(list)

list = [1,2,3,4,5]
print(rotate_right2(list, 3))
"""

# 5) Write a function, median, that takes a list of numbers and 
#    returns the median value.
#
#    For example, median([2, 3, 1]) should return 2.

import math

def median(list):
    size = len(list)
    if size % 2 == 0:
        middle2 = int(size / 2)
        middle1 = int((size / 2) - 1)
    else:
        middle1 = math.trunc(size / 2)
        middle2 = middle1

    list.sort()
    med = (list[middle1] + list[middle2]) / 2.0    
    print(med)
        
"""   
list = [5,6,4,2,3,1]
median(list) # Expected: (3 + 4) / 2 = 3.5

list = [5,6,4,2,3,1,7]
median(list) # Expected: (4 + 4) / 2 = 4.0
""" 