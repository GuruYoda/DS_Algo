
	
"""iterative approach 
Python list to search through, and the value

Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    if len(input_array) == 1:
        if input_array[0] == value:
            return 0
            
    if len(input_array) >= 2:
        l = len(input_array)
       
        mid = 0
        if l%2 == 0:
            mid = l/2
        else:
            mid = (l+1)/2
        
        
        while mid <= l and mid >= 0:
            
            if value == input_array[mid-1]:
                return mid-1
            
            if value > input_array[mid-1]:
             
                if mid%2 == 0 and l%2 == 0:
                    mid = int(mid + (l-mid)/2)
                    if mid == l:
                        if input_array[mid-1] == value:
                            return mid-1
                        else:
                            return -1
                else:
                    mid = int(mid + (l-mid+1)/2)
                    if mid == l:
                        if input_array[mid-1] == value:
                            return mid-1
                        else:
                            return -1
                
            elif value < input_array[mid-1]:
               
                if mid%2 == 0:
                    l = mid
                    mid = int(mid/2)
                    if mid == l:
                        if input_array[mid-1] == value:
                            return mid-1
                        else:
                            return -1
                else:
                    l = mid
                    mid = int((mid + 1)/2)
                    if mid == l:
                        if input_array[mid-1] == value:
                            return mid-1
                        else:
                            return -1
           

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)