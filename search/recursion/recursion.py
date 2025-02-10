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
# Decimal to binary

def decimal_to_binary(k):
    # End condition
    if k == 1:
        return str(1)
    
    # Recursion condition
    quotient = k // 2
    smaller_output = decimal_to_binary(quotient)
    
    current_output = str(k % 2)

    return smaller_output + current_output

example_decimal = 11
result = decimal_to_binary(example_decimal)
print(result)

# Example 3
# Checking palindrome

def is_palindrome(s):
    if len(s) <= 1: 
        return True
    
    if s[0] != s[-1]:
        res = False
    else:
        res = is_palindrome(s[1:-1])
    
    return res

res = is_palindrome("a")
print(res)