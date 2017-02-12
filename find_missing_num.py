'''Given a list of numbers from 1 to n, find a missing number.'''

def find_missing_num(numbers, n):
    expected_sum = (n * (n+1))/2 

    actual_sum = 0
    for num in numbers:
        actual_sum+=num
    
    return expected_sum-actual_sum


# Main #

numbers = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
print "Missing number: ", find_missing_num(numbers, 11)

