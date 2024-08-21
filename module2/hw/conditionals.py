# ********************************* Conditionals *********************************

# 1) Write a function that takes the radius of a circle centered 
#    on the origin and an x, y coordinate and returns True if the 
#    point is in the circle and false otherwise.

def valid(radius, x, y):
    # equation for circle, x^2 + y^2 = radius^2
    if (x**2 + y**2) == radius**2:
        return True
    else:
        return False
    
"""
print(valid(2,0,2))
"""

# 2) Write a function, string_time, that takes three inputs,
#    the number of hours, minutes, and seconds since midnight,
#    and returns a string that represents the time in 12 hour 
#    format with AM or PM at the end. 
#
#    If the input is larger than a single day (or is for the
#    previous day) you should print an error and return an
#    empty string.
#
#    If the input represents midnight or noon, you should return
#    "Midnight" or "Noon" instead of "12:00:00 AM" or "12:00:00 PM"
#
#    For example, string_time(0, 0, 1) should return "12:00:01 AM"
#    and string_time(23, 0, 0) should return "11:00:00 PM"

def string_time(hours, mins, secs):
    #invalid responses: > 24 hrs, >= 60 mins, >= 60 secs, < 0 hrs, < 0 mins, < 0 secs
    valid = False
    zone = ""
    if (hours >= 24) or (mins >= 60) or (secs >= 60) or (hours < 0) or (mins < 0) or (secs < 0):
        print("Invalid")
    else:
        valid = True
        if hours > 12:
            hours = hours % 12
            zone = "PM"
        elif hours == 12:
            hours = 12
            zone = "PM"
        else:
            zone = "AM"
    
    if valid:
        print(hours,":",mins,":",secs, zone)
    
""""    
TEST_CASES = [(12,0,0),(0,0,0),(12,27,21),(7,9,9),(13,39,31),(23,59,59),(0,21,43),(1,5,3),(11,10,10),(12,0,2)]    
for (x,y,z) in TEST_CASES:
    string_time(x,y,z)
"""
    
# 3) Write a function, blackjack2, that takes 2 cards as input 
#    and returns the highest value of a blackjack hand with those 
#    2 cards in it.
#
#    In blackjack, number cards are worth their face value,
#    face cards are worth 10 and and Ace can be worth 1 or 11.  You
#    choose the value of the Ace to make the value of the hand as
#    high as possible without going over 21.
#
#    As the suit is irrelevant, assume that each card is represented
#    as a single character from the string "23456789TJQKA"
#
#    Look in the docs for various functions on strings that might
#    be useful.
#
#    For example, blackjack2("5", "K") should return 15.

def blackjack2(card1, card2):
    if (card1 == '2') or (card1 == '3') or (card1 == '4') or (card1 == '5') or (card1 == '6') or (card1 == '7') or (card1 == '8') or (card1 == '9'):
        card1_value = int(card1)
    elif (card1 == 'T') or (card1 == 'J') or (card1 == 'Q') or (card1 == 'K'):
        card1_value = 10
    elif (card1 == 'A'):
        card1_value = 11
    else:
        print("Invalid card")
        
    if (card2 == '2') or (card2 == '3') or (card2 == '4') or (card2 == '5') or (card2 == '6') or (card2 == '7') or (card2 == '8') or (card2 == '9'):
        card2_value = int(card1)
    elif (card2 == 'T') or (card2 == 'J') or (card2 == 'Q') or (card2 == 'K'):
        card2_value = 10
    elif (card2 == 'A'):
        card2_value = 11 
    else:
        print("Invalid card")
        
    return card1_value + card2_value

"""
print(blackjack2('2', 'T'))
"""

# 4) Write a function, blackjack3, that takes 3 cards as input 
#    and returns the highest value of a blackjack hand with those 
#    3 cards in it.  The result should not be greater than 21, if
#    that is possible.
#
#    Think carefully about how this is different than blackjack2.
#
#    For example, blackjack3("5", "K", "5") should return 20.

def blackjack3(card1, card2, card3):
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return [10]
        elif card == 'A':
            return [1,11]
        else:
            return [int(card)]
        
    values1 = card_value(card1)
    values2 = card_value(card2)
    values3 = card_value(card3)
    
    # Use cartesian product to calculate possible sums
    possible_sums = {v1 + v2 + v3 for v1 in values1 for v2 in values2 for v3 in values3}
    
    valid_sums = [s for s in possible_sums if s <= 21]
    
    return max(valid_sums)

"""
print(blackjack3("5", "K", "5"))  # Should return 20
print(blackjack3("A", "A", "9"))  # Should return 21
print(blackjack3("A", "8", "2"))  # Should return 21
print(blackjack3("J", "Q", "A"))  # Should return 21
print(blackjack3("A", "A", "A"))  # Should return 13
"""

### Optional Bonus Questions

# 5) Write a function, string_date, that takes 3 arguments,
#    the month, day, and year as numbers, and returns the
#    date as a string in human readable form.
#
#    You may assume that the month, day, and year are valid.
#
#    For example, string_date(1, 1, 2013) should return
#    "January 1st, 2013".

def string_date(month, day, year):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    # Determine the appropriate suffix for the day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    
    # Construct the human-readable date string
    date_str = f"{months[month - 1]} {day}{suffix}, {year}"
    
    return date_str

"""
print(string_date(1, 31, 2013)) 
"""

# 6) Write a function, next_date, that takes 3 arguments,
#    the month, day, and year as numbers, and returns the
#    following date as a string in human readable form.
#
#    You may assume that the month, day, and year are valid.
#
#    For example, next_date(1, 1, 2013) should return 
#    "January 2nd, 2013".

def is_leap_year(year):
    # Check if the year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def next_date(month, day, year):
    # Number of days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust for leap year
    if is_leap_year(year):
        days_in_month[1] = 29
    
    # Increment the day
    day += 1
    
    # Check if we need to move to the next month
    if day > days_in_month[month - 1]:
        day = 1
        month += 1
    
    # Check if we need to move to the next year
    if month > 12:
        month = 1
        year += 1
    
    # Use the string_date function to format the next date
    return string_date(month, day, year)

def string_date(month, day, year):
    # List of month names
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    # Determine the appropriate suffix for the day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    
    # Construct the human-readable date string
    date_str = f"{months[month - 1]} {day}{suffix}, {year}"
    
    return date_str

"""
print(next_date(1, 31, 2013))  # Output: "January 2nd, 2013"
"""