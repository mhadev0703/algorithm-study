# Finding the maximum value
arr = [1, 2, 4, 6, 1, 2, 3]
max_value = float("-inf")

for ele in arr:
    if ele > max_value:
        max_value = ele

print(max_value)
# -> 6

# Callback function
def caller(func, n):
    return func(n)

# Declaring two callback functions
def square(n):
    return n*n

def minus_one(n):
    return n-1

print(caller(square, 10))
# -> 100
print(caller(minus_one, 10))
# -> 9

# Converting all of elements into an integer
arr = ['1', '3', '7', '10', '33']
res = list(map(int, arr))   # Integer conversion built-in function 
print(res)
# -> [1, 3, 7, 10, 33]

# If element is greater than 100, return -1
arr = [1, 201, 44, 33, 2, 105]

def over_hundred(n):
    if n > 100:
        return -1
    else:
        return n
    
res = list(map(over_hundred, arr))
print(res)
# -> [1, -1, 44, 33, 2, -1]

# sorted() function example
set_numbers = (8, 3, 9, 1, 5)

# sorted() sorts iterable (set in this case), and converts it into list
unique_numbers = sorted(set_numbers)
print("Ascending order:", unique_numbers)
# -> [1, 3, 5, 8, 9]

# Case of descending order
unique_numbers = sorted(set_numbers, reverse = True)
print("Descending order:", unique_numbers)
# -> [9, 8, 5, 3, 1]

# Takes name and score, then zip it & convert it into list, sort in descending order

l1 = ['Amy', 'Cam', 'Bob']  
l2 = [81, 62, 79]

zipped = list(zip(l1, l2))
print(zipped)
# -> [('Amy', 81), ('Cam', 62), ('Bob', 79)]
print(sorted(zipped))
# -> [('Amy', 81), ('Bob', 79), ('Cam', 62)]

# To sort tuple by the second element, 
# takes tuple as input then define function returning the second element
def sort_by_second(tup):
    return tup[1]

# As the parameter of sorted(), put key = function name
print(sorted(zipped, key = sort_by_second))
# -> [('Cam', 62), ('Bob', 79), ('Amy', 81)]
print(sorted(zipped, key = sort_by_second, reverse = True))  # Descending order
# -> [('Amy', 81), ('Bob', 79), ('Cam', 62)]