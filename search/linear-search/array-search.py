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

