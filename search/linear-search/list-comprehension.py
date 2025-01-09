# Make an array initialized with 0 using range
# _ is used when we focus on the number of iteration, without using 'i'
arr = [ 0 for _ in range(10) ] 
# -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Make an array based on the user input
arr = [ int(input()) for _ in range(5) ]
"""
1
2
3
4
5
[1, 2, 3, 4, 5]
"""

# Make an array after referring another array
arr = [1, 2, 3, 4, 5]
arr2 = [ element * 2 for element in arr ]
# -> [2, 4, 6, 8, 10]

# Make a new array with conditions: 
# Even number -> Negative number & Leave odd number unchanged
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_arr = [ -element if element % 2 == 0 else element for element in arr ]
# -> [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

# Add two elements from two arrays in order
arr1 = [100, 200, 300]
arr2 = [1, 2, 3]
arr3 = [ arr1[i] + arr2[i] for i in range(len(arr1)) ]
# -> [101, 202, 303]

# Add two elements in every possible cases, make an array length of arr1 * arr2
arr1 = [100, 200, 300]
arr2 = [1, 2, 3]
arr3 = [ ele1 + ele2 for ele1 in arr1 for ele2 in arr2 ]
# -> [101, 102, 103, 201, 202, 203, 301, 302, 303] 

# Make 2D array initialized with '0' (N rows and M columns)
N, M = 3, 5
arr_2D = []  # Empty list

for i in range(N): 
		row = []  # Empty list to be used as inner list
		for j in range(M):
				row.append(0)  # Add '0' into inner list
				
		arr_2D.append(row)  # Add inner list into entire 2D list
		
print(arr_2D)
# -> [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]		

# Print 2D array easily 
# *[list]
print(*['A', 'B', 'C'])
# -> A B C
print('A', 'B', 'C')
# -> A B C 
print(*arr_2D)
# -> [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
print('A', 'B', 'C', sep="\n")
"""
A
B
C
"""

print(*arr_2D, sep="\n")
"""
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
"""

# Make 2D array initialized with '0' (N rows and M columns)
N, M = 3, 5
arr_2D = [[0 for _ in range(M)] for _ in range(N)]
print(*arr_2D, sep="\n")
"""
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
"""

# Wrong case for making a 2D array initialized with '0'
arr = [[0] * 4]  