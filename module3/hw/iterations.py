#  IMPORTANT:  You may not use the range function for any of these
#               problems!  This restriction is only for today.
#

#1  Using only list comprehensions and no loops, write a function, div3or7,
#   that takes a list of numbers and returns a list that only includes the 
#   numbers from the input list that are divisable by either 3 or 7.

def div3or7(list):
    return [num for num in list if (list[num-1] % 3 == 0) or (list[num-1] % 7 == 0)]

"""
example_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(div3or7(example_list))
"""

#2  Write a function, useless, that takes a single number as input.
#   Take all numbers between 0 and the input number and multiply them
#   by 2.  Return a list that contains the first ten (or fewer, if
#   there aren't 10) of the resulting numbers that are divisible by 3.
#
#   For example, useless(72) should return 
#           [0, 6, 12, 18, 24, 30, 36, 42, 48, 54]

def useless(num):
    multiply_list = []
    for i in range(num + 1):
        multiply_list.append(i *2)

    div_list = []
    j = 0
    while len(div_list) < 10:
        if multiply_list[j] % 3 == 0:
            div_list.append(multiply_list[j])
        j += 1
            
    return div_list

"""
random_num = 72
print(useless(random_num))
"""

#3  Write a function, make_map, which takes two equal length lists and
#   returns a dictionary mapping items in corresponding positions from
#   the first list to the second.
#
#   For example, make_map([1, 2, 3], ['a', 'b', 'c']) should return
#     {1: 'a', 2: 'b', 3: 'c'}

def make_map(list1, list2):
    dict = {}
    for i in range(len(list1)):
        dict[list1[i]] = list2[i]
        
    return dict

"""
list1 = [1,2,3]
list2 = ['a','b','c']
print(make_map(list1, list2))
"""

#4  Write a function, rotate_smallest, that "rotates" a list to the
#   left until the smallest element is the first element in the list.
#
#   For example, the following program should print [2, 5, 16, 8]:
#      lst = [16, 8, 2, 5] 
#      rotate_smallest(lst)
#      print(lst)

def rotate_smallest(list):	
    # Get the smallest number in the list
    smallest = list[0]
    for i in range(len(list)):
        if list[i] < smallest:
            smallest = list[i]
    
    for j in range(len(list)):
        if list[0] == smallest:
            break
        else:
            temp = list[0]
            for s in range(len(list) -1):
                list[s] = list[s + 1] 
            list[len(list) - 1] = temp
    return list

"""
example_list = [16, 8, 2, 5]
print(rotate_smallest(example_list))
"""

#5  You have a credit at a store that expires tomorrow, so you want
#   to use it all.  Write a function, buy, that takes the amount of
#   the credit and a list of prices of the available items in the
#   store.  You want to buy two items whose total price is exactly
#   equal to your available credit.   Assume that this is always
#   possible.  Return a 2-element list containing the indices of
#   the two items you should buy.
#
#   For example, buy(200, [100, 150, 79, 99, 3, 50, 345]) should
#   return [1, 5]

def buy(credit, list):
    indices = []
    for i in range(len(list)):
        for j in range(len(list) - i):
            if list[i] + list[j] == credit and i != j:
                indices.append(i)
                indices.append(j)
                return indices
    return "No combination"

"""
print(buy(200, [100, 150, 79, 99, 3, 50, 345]))
"""

#6  Write a function, collatz, to test the Collatz conjecture.  Your
#   function should take a single positive number as input.  You
#   should then execute the following process:
#     - if the number is even, divide it by 2 
#     - if the number is odd, triple it and add 1 
#
#   You should repeat this until the result is 1 (the Collatz
#   conjecture says this will always reach 1 no matter what positive
#   integer you start with).  Return the number of steps it takes to
#   get to 1.
#
#   Test your function on some inputs.  collatz(27) should return
#   111, for example.  What are the largest numbers that show up
#   along the way?

import random

def collatz(num):
    print(num)
    counter = 0
    while (num != 1):
        if (num % 2 == 0):
            num /= 2
        else:
            num *= 3
            num += 1
        counter += 1
    return counter

"""
random_num = random.randint(1,1000)
print(collatz(random_num))
"""