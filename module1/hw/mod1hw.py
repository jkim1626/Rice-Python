# 1) A chemist has 75 ml of a 40% acid solution.  How much water should
#    she add to make a 15% acid solution?

print("Problem #1")

old_volume = 75
acid = 0.4 * 75
proportion = acid / 15
new_volume = proportion * 100
change = new_volume - old_volume 

print("She should add", change, "ML of water")

# 2) The Rumbler roller coaster consists of one train of linked 2-person
#    cars.  Each ride takes 1 minute and 45 seconds.  It takes 45
#    seconds for each group to board the coaster and 30 seconds to get
#    off.  If 520 people ride the Rumbler in one hour, how many cars
#    does the coaster have?

print("\nProblem #2")

total_time_in_seconds = 1*60*60
ride_in_seconds = 60 + 45
board_in_seconds = 45
exit_in_seconds = 30

rotations = total_time_in_seconds / (ride_in_seconds + board_in_seconds + exit_in_seconds)
total_people = 520

# total people = (cars per rotation) * (people per car) * (num rotations)
car_per_rotation = total_people / (2 * rotations)

print("Number of cars in The Rumbler is", int(car_per_rotation))

# 3) Compute the number of ways to choose 3 balls out of 100 balls.

print("\nProblem #3")

n = 100
n_fact = 1
for i in range(n):
    temp = i + 1
    n_fact = n_fact * temp
  
r = 3
r_fact = 1
for i in range(r):
    temp = i + 1
    r_fact = r_fact * temp
    
sub = n - r
sub_fact = 1
for i in range(sub):
    temp = i + 1
    sub_fact = sub_fact * temp
    
print("Number of ways to choose 3 balls out of 100 is", int(n_fact / (r_fact * sub_fact)))

# 4) Derive an expression for yval in terms of xval that represents a
#    line through the two points (4, -1) and (3, -6).  Compute the
#    value of yval when xval is 0

print("\nProblem #4")

change_in_y = -6 - (-1) 
change_in_x = 3 - 4 
slope = change_in_y / change_in_x

print("The general equation for the line is y + 6 =", int(slope), "(x - 3)")

yval = (5*(0-3)) -6

print("The value of y when x is 0:", yval)

# 5) You start with "principal" dollars.  Each year, you are paid
#    interest at a rate of "interest" percent interest.  Write an
#    expression that evaluates to the total amount you would have at
#    the end of "period" years.  Compute this value for principal =
#    1000, interest = 5%, and period = 10.

print("\nProblem #5")
print("General formula: (principal)((100 + interest) / 100)^(years)")

total = 1000 * (((100 + 5) / 100) ** 10)
print("Total pay after 10 years, 5% interest, and principal of 1000 =", round(total, 2))

# 6) Compute the value of 10 factorial.

print("\nProblem #6")
nums = 10
total = 1
for i in range(nums):
    temp = i + 1
    total = total * temp
print("10! =", total)

# 7) Give a formula for the surface area of a rectangular right prism.
#    Your answer should give a result for the surface area in terms of
#    side1, side2, and side3, the three independent side lengths.
#    Compute the surface area of a rectangular right prism where side1
#    is 10, side2 is 20, and side3 is 30.

print("\nProblem #7")
print("General formula for the surface area of a rectangular prism: 2 * ((side1 * side2) + (side1 * side3) + (side2 * side3))")

side1 = 10
side2 = 20
side3 = 30
total = 2 * ((side1 * side2) + (side1 * side3) + (side2 * side3))

print("Surface area of a 10x20x30 rectangular prism:", int(total))

### Optional Bonus Questions

# 8) Give a formula for the sum "sum" of the numbers 0, 1, ..., num.
#    Use your formula to compute sum for num = 100. Hint: The
#    challenging part is coming up with a simple mathematical formula
#    that just uses a few algebraic operations.  Be sure to check your
#    answer on a few examples.

import math
print("\nProblem #8")
num = 15
total1 = 0
for i in range(num + 1):
    total1 = total1 + i
    
num2 = 15
total2 = (num2 + 1) * (num2 / 2)
    
print("Method 1 answer:", int(total1))
print("Method 2 answer:", int(total2))


# 9) Give a formula to approximate e^val (for val less than 1).  Use
#    the first several terms of a power series to do so.  Compute an
#    approximation of e^0.5.
#    For this problem, feel free to look up what a "power series" is.

print("\nProblem #9")
x = 0.5
num = 10
total = 0
subtotal = 0
for i in range(num):    
    temp = (x ** i) / math.factorial(i)
    total = total + temp
    
print("Power series approximation for e^x for x = 0.5 over 4 iterations:", total)