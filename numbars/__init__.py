import random

def add_numbers(one, two):
    return one + two

def subtract_numbers(one, two):
    return one - two

def multiply_numbers(one, two):
    return one * two

def divide_numbers(one, two):
    if (one == 0 or two == 0) or (one == 0 and two == 0): 
        return "Can't Divide by 0!"
    else:
        return one / two

def randomize_numbers(min, max):
    return random.randint(min, max)
