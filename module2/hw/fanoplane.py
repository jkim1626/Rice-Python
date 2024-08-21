# ********************************* Fano Plane *********************************

import comp140_module2 as spotit

# 1) Write a function that takes a list of numbers as input
#    and returns the product of all the numbers in the list.

import math
def product(list):
    total = 1
    for i in range(len(list)):
        temp = list[i]
        total = total * temp
    print("Product of all the numbers in the list:", total)

"""    
list = [1,2,3,4,5]
product(list)
"""

# 2) Manually build the Fano plane as a Spot it! deck 
#    represented as a list of lists, by filling in the list
#    below.  (In other words, hard-code the appropriate
#    numbers in the lists.)  Each inner list should be the
#    list of "images" that would appear on that card.  An
#    image should be represented as an integer.  For example,
#    you could choose, 0 = Heart, 1 = Spade, etc.  
#    Comment your choices.

# Create a deck 
deck = []

# 7 images
# spade = 1
# infinity = 2
# sun = 3
# heart = 4
# clover = 5
# rain = 6
# flower = 7
    
# card 1
card = [1,2,3]
deck.append(card)

# card 2
card = [2,4,7]
deck.append(card)

# card 3
card = [2,5,6]
deck.append(card)

# card 4
card = [1,6,7]
deck.append(card)

# card 5
card = [3,4,6]
deck.append(card)

# card 6
card = [3,5,7]
deck.append(card)

# card 7
card = [1,4,5]
deck.append(card)

"""
print(deck)
"""

# 3) Write a function to check that two Spot it! cards
#    have one and only one match.  Assume each card is a
#    list of numbers, as described in problem #2.

def check_cards(deck, n, m):
    count = 0
    check = False
    
    if n == m:
        print("Cards are the same")
        
    for i in range(len(deck[n])):
        for j in range(len(deck[m])):
            if deck[n][i] == deck[m][j]:
                count += 1
                check = True
    return check and count == 1

"""
for i in range(7):
    for j in range(7):
        if i != j:
            print(check_cards(deck, i,j))  
"""                     

# 4) Write a function that checks if a list of lists
#    represents a valid deck of Spot it! cards.  It should
#    return True if it is and False otherwise.  It should
#    return True for your answer to #2 above.  You should try
#    other inputs, as well.

def valid(deck):
    for i in range(len(deck)):
        for j in range(len(deck)):
            if i != j:
                valid = check_cards(deck, i,j)
                if valid != True:
                    return False
    return True

"""
deck4 = [
    [1, 2, 3, 4, 5],
    [1, 6, 7, 8, 9],
    [2, 6, 10, 11, 12],
    [3, 7, 10, 13, 14],
    [4, 8, 11, 13, 15]
]

print(valid(deck4))

deck2 = [
    [1, 2, 3, 4],
    [1, 5, 6, 7],
    [2, 5, 8, 9],
    [3, 6, 8, 10]
]

print(valid(deck2))
"""

# 5) If your deck is valid, you should be able to play the
#    game.  You can try it by calling spotit.start(deck),
#    where deck is your list of lists from #2.

spotit.start(deck)