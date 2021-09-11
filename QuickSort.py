"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()
        
    array_small = []
    array_large = []
    
    for item in array:
        if item < pivot:
            array_small.append(item)
            
        else:
            array_large.append(item)
            
    return quicksort(array_small) + [pivot] + quicksort(array_large)


if __name__ == "__main__":
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print (quicksort(test))