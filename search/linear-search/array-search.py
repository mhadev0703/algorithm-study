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

# Using lambda function as parameter of map() function
# Takes list as input, then return list after squaring each element
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda x : x*x, input_list))
print(result)
# -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Takes name and score list, sort by descending order
arr = [('Amy', 81), ('Cam', 62), ('Bob', 79)]

# Using lambda function as parameter of sorted()
print(sorted(arr, key = lambda x : x[1], reverse = True))
# -> [('Amy', 81), ('Bob', 79), ('Cam', 62)]


# Example 1: Student info in 2D list
students = [
    ["John", 85],
    ["Jane", 92],
    ["Dave", 88],
    ["Sara", 95]
]

# Sort students by score in descending order
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)
# -> [['Sara', 95], ['Jane', 92], ['Dave', 88], ['John', 85]]

# Example 2
import sys

inp = int(input())
for i in range(inp):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# Example 3
N = int(input())
pairs = [ list(map(int, input().split())) for _ in range(N) ]

output = [0] * N

for i in range(N):
    output[i] = sum(pairs[i])

print(*output, sep="\n")
"""
Input
5
1 1 
12 34
5 500
40 60
1000 1000

Output
2
46
505
100
2000
"""

# Example 4
"""
Program that reads 10 numbers, calculates their remainder when divided by 42, 
and counts the number of unique remainders.

Input
1
2
3
4
5
6
7
8
9
10

Output
10
"""

# Solution 1
# Read 10 input numbers and compute their remainder when divided by 42
remainders = set()

for _ in range(10):
    num = int(input())  # Read each number
    remainders.add(num % 42)  # Store the remainder in a set

# Output the count of unique remainders
print(len(remainders))

# Solution 2
arr = [42, 84, 252, 420, 840, 126, 42, 84, 420, 126]
arr_42 = list(map(lambda ele: ele % 42, arr))
arr_42_unique = list(set(arr_42))
print(arr_42)