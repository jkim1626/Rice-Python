def pick_a_number(board, score1 = 0, score2 = 0, player = 1):
    """
    Pick a number game. Two players choose between the first and last
    numbers from a list of numbers. Winner is the highest sum. 
    """
    if len(board) == 0:
        return (score1, score2)
    
    if len(board) == 1:
        if player == 1:
            return (score1 + board[0], score2)
        else:
            return (score1, score2 + board[0])
    
    # Player 1's turn
    if player == 1:
        # Pick the first number
        first_choice = pick_a_number(board[1:], score1 + board[0], score2, 2)
        # Pick the last number
        last_choice = pick_a_number(board[:-1], score1 + board[-1], score2, 2)
    # Player 2's turn
    else:
        # Pick the first number
        first_choice = pick_a_number(board[1:], score1, score2 + board[0], 1)
        # Pick the last number
        last_choice = pick_a_number(board[:-1], score1, score2 + board[-1], 1)
    
    # Return the result where the first player's score is maximized
    if player == 1:
        return max(first_choice, last_choice, key=lambda x: x[0])
    else:
        return max(first_choice, last_choice, key=lambda x: x[1])

# board = [8, 2, 5, 3, 9, 1, 4, 2]
# print(pick_a_number(board))
# (26,8)







"""
More Recursion 
"""

def search(list, low, high, item):
    """
    Binary Search Algorithm 
    """
    
    if high >= low:
        mid = (high + low) // 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            return search(list, low, mid - 1, item)
        else:
            return search(list, mid + 1, high, item)
    else:
        return -1        
                
"""               
list = [1,2,3,4,5,6,7,8,9,10]
low = 0
high = len(list) - 1
item = 6
print("Index of item in list: ", search(list, low, high, item))
"""

def deep_list_copy(lst):
    """
    Creates a deep copy of a list with nested lists
    """
    if len(lst) == 0:
        return []
    new_list = []
    for item in lst:
        if isinstance(item, list):
            new_list.append(deep_list_copy(item))
        else:
            new_list.append(item)
    return new_list

"""
lst1 = [1, 2, [1, 2], [1, 2, 3], [[1]], 4]
lst2 = deep_list_copy(lst1)
lst2.append(5)
print(lst1)  # Should print: [1, 2, [1, 2], [1, 2, 3], [[1]], 4]
print(lst2)  # Should print: [1, 2, [1, 2], [1, 2, 3], [[1]], 4, 5]
"""


def merge(new_list, list1, list2):
    """
    Merges and prints two sorted lists into a single sorted list
    """
    if len(list1) == 0 and len(list2) == 0:
        return new_list    
    elif len(list1) == 0:
        for i in range(len(list2)):
            new_list.append(list2[i])
    elif len(list2) == 0:
        for i in range(len(list1)):
            new_list.append(list1[i])
    else:
        start1 = list1[0]
        start2 = list2[0]
        if start1 < start2:
            list1 = list1[1:]
            new_list.append(start1)
            merge(new_list, list1, list2)    
        else:
            list2 = list2[1:]
            new_list.append(start2)
            merge(new_list, list1, list2)    
    
    return new_list

# print(merge([], [1,4,9],[2,6,8]))
# Should print [1,2,4,6,8,9]
# print(merge([],[7, 19, 22], [1, 2, 3]))
# Should print [1, 2, 3, 7, 19, 22]
# print(merge([], [8, 10, 12, 14, 16], [9]))
# Should print [8, 9, 10, 12, 14, 16]

def powerset(lst):
    """
    Takes a list of unique numbers and returns the power set of the members in the list
    """    
    if len(lst) == 0:
        return [[]]
    
    # Get the power set of the list excluding the last element
    subsets_without_last = powerset(lst[:-1])
    
    # Add the last element to each subset from the above power set
    subsets_with_last = [subset + [lst[-1]] for subset in subsets_without_last]
    
    # Combine the subsets without the last element and with the last element
    return subsets_without_last + subsets_with_last
            
    
# print(powerset([1,2]))
# Should print [[], [1], [2], [1, 2]]
# print(powerset([1, 2, 3]))
# Should print [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
# print(powerset([1, 2, 3, 4]))
# Should print [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]