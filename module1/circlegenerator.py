"""
Problem:
In this assignment, you will solve the following problem: given three points, calculate the center and radius of a circle that passes through all three points.
"""

def calc_distance(a, b, a1, b1):
    distance = (((a1 - a)**2) + ((b1 - b)**2)) ** (1 / 2)
    return distance

def calc_midpoint(a, b, a1, b1):
    mid_point_a = a + ((a1 - a) / 2)
    mid_point_b = b + ((b1 - b) / 2)
    return mid_point_a, mid_point_b

def calc_slope(a, b, a1, b1):
    slope = (b1 - b) / (a1 - a)
    return slope

def calc_perp_slope(slope):
    perp_slope = -1/slope
    return perp_slope

def calc_intersect(a,b,s,a1,b1,s1):
    intersect_a = ((s*a) - (s1*a1) + (b1-b)) / (s-s1) 
    intersect_b = s * (intersect_a - a) + b
    return intersect_a, intersect_b


a1x = int(input("Enter a x point for point 1"))
a1y = int(input("Enter a y point for point 1"))

a2x = int(input("Enter a x point for point 2"))
a2y = int(input("Enter a y point for point 2"))

a3x = int(input("Enter a x point for point 3"))
a3y = int(input("Enter a x point for point 3"))

mid1x, mid1y = calc_midpoint(a1x, a1y, a2x, a2y)
mid2x, mid2y = calc_midpoint(a1x, a1y, a3x, a3y)

slope1 = calc_slope(a1x, a1y, a2x, a2y)
slope2 = calc_slope(a1x, a1y, a3x, a3y)

perp_slope1 = calc_perp_slope(slope1)
perp_slope2 = calc_perp_slope(slope2)

intersectx, intersecty = calc_intersect(mid1x, mid1y, perp_slope1, mid2x, mid2y, perp_slope2)

radius = calc_distance(intersectx, intersecty, a1x, a1y)

print("Equation for circle: (x -", intersectx,")^2 + (y -", intersecty,")^2 = ",radius**2)


""""
Using CodeSkulptor GUI (library exclusive to rice students):

import comp140_module1 as circles

def calc_distance(a, b, a1, b1):
    distance = (((a1 - a)**2) + ((b1 - b)**2)) ** (1 / 2)
    return distance

def calc_midpoint(a, b, a1, b1):
    mid_point_a = a + ((a1 - a) / 2)
    mid_point_b = b + ((b1 - b) / 2)
    return mid_point_a, mid_point_b

def calc_slope(a, b, a1, b1):
    slope = (b1 - b) / (a1 - a)
    return slope

def calc_perp_slope(slope):
    perp_slope = -1/slope
    return perp_slope

def calc_intersect(a,b,s,a1,b1,s1):
    intersect_a = ((s*a) - (s1*a1) + (b1-b)) / (s-s1) 
    intersect_b = s * (intersect_a - a) + b
    return intersect_a, intersect_b

def make_circle(a1x, a1y, a2x, a2y, a3x, a3y):
    mid1x, mid1y = calc_midpoint(a1x, a1y, a2x, a2y)
    mid2x, mid2y = calc_midpoint(a1x, a1y, a3x, a3y)
    slope1 = calc_slope(a1x, a1y, a2x, a2y)
    slope2 = calc_slope(a1x, a1y, a3x, a3y)
    perp_slope1 = calc_perp_slope(slope1)
    perp_slope2 = calc_perp_slope(slope2)
    intersectx, intersecty = calc_intersect(mid1x, mid1y, perp_slope1, mid2x, mid2y, perp_slope2)
    radius = calc_distance(intersectx, intersecty, a1x, a1y)
   
    return intersectx,intersecty,radius


circles.start(make_circle)
"""