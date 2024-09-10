# `is_even` function

# You are defining is_even with the arguement of number
def is_even(number):
# This is saying if the number is divisble by 2 (% Modular Operator) then it is equal to 0   
    if (number % 2) == 0:
# If the number is divisble by 2, then it is equal to zero, which will return with True
        return True
# If the number is not divisible by 2, then it is not equal to zero, which will return a False
    else:
        return False

print(is_even(6))
print(is_even(105))


# `is_odd` function

def is_odd(number):
    if (number % 2) != 0:
        return True
    else:
        return False

print(is_odd(11))
print(is_odd(42))

# `only_evens` function

def only_evens(numbers):
    i = 0
    even_numbers = []
    while i < len(numbers):
        if (numbers[i] % 2) == 0:
            even_numbers.append(numbers[i])
        i = i + 1
    return even_numbers

print(only_evens([11, 20, 42, 97, 23, 10]))

# `only_odds` function

# Version 1: Using a `while` loop

def only_odds_while(numbers):
    i = 0
    odd_numbers = []
    while i < len(numbers):
        if (numbers[i] % 2) != 0:
            odd_numbers.append(numbers[i])
        i = i + 1
    return odd_numbers

print(only_odds_while([11, 20, 42, 97, 23, 10]))

# Version 2: Using a `for` loop

def only_odds_for(numbers):
    odd_numbers = []
    for n in numbers:
        if (n % 2) != 0:
            odd_numbers.append(n)
    return odd_numbers

print(only_odds_for([11, 20, 42, 97, 23, 10]))