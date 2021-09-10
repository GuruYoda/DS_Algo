'''
The following is an implementation of the 
basic data structure LINKED-LIST
'''

class Node(object):
    """the Node is the base of the linked list 
    it contain the information like the 
    value of the node and the pointer to the 
    next Node"""
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
       
    def append(self, new_element):
        """the basic append function that runs in 
        constant time and adds the new Node 
        at the end of the linked list"""
        current = self.head
        if (self.head):
            while(current.next):
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an Node from a particular position.
        Assume the first position is "1".
        Return None if position is not in the list."""
        current = self.head
        if self.head:
            i = 1
            while current:
                if position == i:
                    return current
                current = current.next
                i += 1
        
        return None

    
    def insert (self, new_Node, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd Nodes."""
        current = self.head
        if position == 1:
            tmp = self.head
            self.head = new_Node
            head.next = tmp
            
        else:
            if self.head:
                i = 1
                while current:
                    if i == position - 1:
                        tmp = current.next
                        current.next = new_Node
                        current.next.next = tmp
                    current = current.next
                    i += 1
            else:
                raise Exeption("Position does not exist in the list")
                
            
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
                
if __name__ == "__main__":                
    # Test cases
    # Set up some Elements
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    print (ll.head.next.next.value)
    # Should also print 3
    print (ll.get_position(3).value)

    # Test insert
    ll.insert(e4,3)
    # Should print 4 now
    print (ll.get_position(3).value)


    # Test delete
    ll.delete(1)
    # Should print 2 now
    print (ll.get_position(1).value)
    # Should print 4 now
    print (ll.get_position(2).value)
    # Should print 3 now
    print (ll.get_position(3).value)
    
                
                
                    
        
        