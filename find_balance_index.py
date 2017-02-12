'''Given an unsorted list of numbers, identify all indexes if exist 
at which sum of left and right subarrays are equal.'''

def find_balance_index(nums):

    if len(nums)<3:
        return

    else: 

        eq_indx = []
        # find the sum of the whole list
        total_sum = 0
        for n in nums:
            total_sum+=n
        print "Total: ", total_sum

        left_sum = 0
        for i in range (0, len(nums)):
            if i == 0:
                left_sum += nums[i]
                continue

            right_sum = total_sum - left_sum - nums[i]
            print "left_sum ", left_sum
            print "right_sum ", right_sum

            if right_sum == left_sum:
                eq_indx.append(str(i))
            
            left_sum +=nums[i]


        return eq_indx


# Main #
numbers = []
eq_indx = find_balance_index(numbers)
if eq_indx:
    print "Balance indexes: ", ",".join(eq_indx)
else:
    print "Balance indexes were not found."
            

    