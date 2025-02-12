# Example 1
# Countdown from 5 to 1
# Output: 5, 4, 3, 2, 1 end!

def countdown(n) :
    if n == 1:
        return "1 end!"
    
    next_count = countdown(n - 1)  # Recursive call for the next number  
    current_number = str(n)  # Convert current number to string

    result = current_number + ', ' + next_count  # Combine current and recursive output
    return result
    
countdown(5)
# -> '5, 4, 3, 2, 1 end!'

# Example 2
# Decimal to binary (Recursion) 

def decimal_to_binary(k):
    # End condition
    if k == 1:
        return str(1)
    
    # Recursive step: Divide n by 2 and convert the quotient first
    next_value = decimal_to_binary(k // 2)  # Convert the quotient to binary
    remainder = str(k % 2)  # Get the remainder as the current binary digit

    return next_value + remainder

example_decimal = 11
result = decimal_to_binary(example_decimal)
print(result)

# Example 3
# Checking palindrome

def is_palindrome(s):
    # Base case
    if len(s) <= 1: 
        return True
    
    # If first and last characters do not match, it's not a palindrome
    if s[0] != s[-1]:
        return False

    # Recursively check the substring without the first and last characters
    return is_palindrome(s[1:-1])

test_string = is_palindrome("a")
print(test_string)


# Example 4
def flatten(nested_list):
    """
    Recursively flattens a nested list.
    """
    # Base case: If the element is not a list, return it as a single-element list
    if not isinstance(nested_list, list):
        return [nested_list]

    flattened_result = []  # Stores the final flattened list
    for element in nested_list:
        flattened_result += flatten(element)  # Recursively flatten each item

    return flattened_result

print(flatten([1, [2, 3, 4], [5, 6, [7, 8]]]))
# -> Expected output: [1, 2, 3, 4, 5, 6, 7, 8]