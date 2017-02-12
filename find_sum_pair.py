'''Given array find a pair of elements with sum equal to given number.'''

def find_sum_pair(numbers, sum):
   
    numbers_dict = {}
    for n in numbers:
        if not numbers_dict.has_key(n):
            numbers_dict[n] = 1
        else:
            numbers_dict[n]+=1


    for n_key in numbers_dict:
        # find difference between current number and the sum
        # check if difference is in the dictionary
        diff = sum - n_key
        if numbers_dict.has_key(diff):
            print "Found numbers ", n_key, " and ", diff, " which sum equals to ", sum


# Main #
numbers = [6, 12, 2, 7, 11, 3]
find_sum_pair(numbers, 9)


    