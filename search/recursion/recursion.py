# Example 1
# Countdown from 5 to 1
# Output: 5, 4, 3, 2, 1 end!

def countdown(n) :
    if n == 1:
        return "1 end!"
    
    recur_out = countdown(n - 1)
    cur_out = str(n)

    comb_out = cur_out + ', ' + recur_out

    return comb_out

countdown(5)
# -> '5, 4, 3, 2, 1 end!'
