# Defining your function of shortest with the arguement of list of strings
def shortest(list_of_strings):
# Saying that shortest is assigned the value of list of strings with a list of [zero]
    shortest = list_of_strings[0]
# Defining that x is assinged the value of 0
    index = 0
# While x is less than the length of list of strings
    while index < len(list_of_strings):
        if len(list_of_strings[index]) <= len(shortest):
            shortest = list_of_strings[index]
        index = index + 1
    return shortest

def longest(list_of_strings):
# Longest is assigned the value of list of strings with a zero to start at the beginning
    longest = list_of_strings[0]
# Defining that x is assinged the value of 0
    index = 0
# While x is less than the length of list of strings
    while index < len(list_of_strings):
        if len(list_of_strings[index]) >= len(longest):
            longest = list_of_strings[index]
        index = index + 1
    return longest

some_strings = ['Xenos', 'Emperor', 'Space Marines', 'Psyker', 'Dreadnaught', 'Tyranids']

print(shortest(some_strings))
print(longest(some_strings))