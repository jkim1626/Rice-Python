# Higher-order Functions

def double(val):
    return 2 * val

def square(val):
    return val ** 2

print(double(3))
print(square(3))

def twice(func, val):
    return func(func(val))

print(twice(double, 3))
print(twice(square, 3))

data = [1, 3, 6, 9, 18]

newdata = [double(item) for item in data]
print(newdata)

newdata2 = map(square, data)
print(list(newdata2))

def even(val):
    if val % 2:
        return False
    else:
        return True
    
newdata3 = filter(even, data)
print(list(newdata3))





# Area under curve

def area(func, low, high, stepsize):
    total = 0.0
    loc = low
    while loc < high:
        total += func(loc) * stepsize
        loc += stepsize
    return total

def f(x):
    return x

def g(x):
    return x ** 2

print(area(f, 0, 10, .01))
print(area(g, 0, 10, .0001))

def h(x):
    if x < 3:
        return x
    elif x < 7:
        return x ** 2
    else:
        return 7 * x - 4

print(area(h, 0, 10, .001))

