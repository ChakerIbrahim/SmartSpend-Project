# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def big_size(n):
    result = []
    for i in n:
        if i > 0:
            result.append("big")
        else :
            result.append(i)
    return result
print(big_size([-1,3,5,-5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
# (Note that zero is not considered to be a positive number).
def count_positive(n):
    result = 0
    for i in n:
        if i > 0:
            result+=1
    n[-1] = result
    return n
print(count_positive([-1,1,1,1]))
    
#Sum Total - Create a function that takes a list and returns the sum of all the values in the list
def sum_total(n):
    result = 0
    for i in n:
        result+= i
    return result
print(sum_total([1,2,3,4]))

# Average - Create a function that takes a list and returns the average of all the values.x
def average(n):
    sum = 0
    for i in n:
        sum += i
        av = sum / len(n)
    return av
print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list
def length(n):
    return len(n)
print(length([3,7,-2,5]))
print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty,
# have the function return False
def minimum(n):
    if len(n) == 0:
        return False
    min = n[0]   
    for i in n:
        if i < min:
            min = i
    return min
print(minimum([3,7,2,5]))   
print(minimum([]))   

      
        # Maximum - Create a function that takes a list and returns the maximum value in the list. 
        # If the list is empty, have the function return False.
def maximum(n):
    if len(n) == 0:
        return False
    max = n[0]
    for i in n:
        if i > max:
            max = i
    return max
print(maximum([3,7,2,5]))   
print(maximum([]))  

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(n):
    if len(n) == 0:
        return False

    return {
        "sum": sum_total(n),
        "avr": average(n),
        "min": minimum(n),
        "max": maximum(n),
        "len": length(n)
    }

print(ultimate_analysis([3,7,2,5]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list
def reverse_list(n):
    result = []
    for i in range(len(n)-1,-1,-1):
        result.append(n[i])
    return result
print(reverse_list([37,2,1,-9]))