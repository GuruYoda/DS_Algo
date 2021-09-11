"""
SORTING ALGORITHMS
"""

"""BUBBLE SORT"""
def bubble(input_list):
     
    """Bubble sort is the slowest sorting
        algorithm available. It works on a verz simple principle
        the position of 2 elements in the lst must swap if the 
        larger lement is befoer the smaller element
        It is O(1) in memory use and O(n*n) in time
        """
   
    tmp = 0
    for i in range(len(input_list)):
        for j in range(len(input_list)-1):
          
            if j ==  len(input_list)-1-i:
                break
            if input_list[j] > input_list[j+1]:
                tmp = input_list[j+1]
                input_list[j+1] = input_list[j]
                input_list[j] = tmp
        
    
    return input_list


input = [21,4,1,3,9,20,25,6,21,14]
bubble = (bubble(input))
print(bubble)    
    