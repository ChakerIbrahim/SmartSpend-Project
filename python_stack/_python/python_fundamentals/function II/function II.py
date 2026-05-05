# Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(n):
    result = []
    for i in range(n,-1,-1):
        result.append(i) 
    return result
print(countdown(5))
# Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
def print_function(n):
    print(n[0])
    return n[1]
print(print_function([1,2]))
# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def sum_first_length(n):
    return n[0] + len(n)
print(sum_first_length([1,2,3,4,5]))
# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values
# from the original list that are greater than its 2nd value. Print how many values this is and then return the new
# list. If the list has less than 2 elements, have the function return False
def value_greater_than_second(n):
    if len(n) < 2:
        return False
    
    second = n[1]
    result = []

    for i in n:
        if i > second:
            result.append(i)
    
    print(len(result))
    return result
print(value_greater_than_second([5,2,3,2,1,4]))
print(value_greater_than_second([3]))
# This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size,
# and whose values are all the given value.
def length_and_value(n,m):
    result = []
    for i in range(n):
        result.append(m)
    return result
print(length_and_value(4,7))
print(length_and_value(6,2))
        

