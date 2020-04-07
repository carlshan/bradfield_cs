"""
Implementation of Linked list
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class List(object):
    """    
    * List() creates a new list that is empty. It needs no parameters and returns an empty list.
    * add(item) adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
    * remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
    * search(item) searches for the item in the list. It needs the item and returns a boolean value.
    * is_empty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.
    * size() returns the number of items in the list. It needs no parameters and returns an integer.
    * append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
    * index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
    * insert(pos, item) adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
    * pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
    * pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, item):
        # adds a new item to the end of the list
        temp = Node(item)
        curr = self.head
        prev = None
        while curr is not None:
            prev = curr
            curr = curr.next
        
        if prev is None: self.head = temp 
        else: prev.next = temp

    def insert(self, pos, item):
        # adds a new item to the list at position pos
        temp = Node(item)
        counter = 0
        curr = self.head
        prev = None

        if pos == 0: # if we are inserting at the first position
            self.head = temp
            temp.next = curr
            return None

        while curr is not None:
            prev = curr
            curr = curr.next
            if pos == counter: # found the position
                temp.next = curr
                prev.next = temp
            counter += 1

    def pop(self, pos=None):
        # if pos is None removes the last item in the list
        # else remove the item at pos
        curr = self.head
        prev = None
        if pos == None:
            # remove and return last item
            while curr.next is not None:
                prev = curr
                curr = curr.next
            
            prev.next = None
        else:
            counter = 0

            if pos == 0:
                result = self.head
                self.head = curr.next
                return result
            
            while counter != pos:
                counter += 1
                prev = curr
                curr = curr.next

            next_node = curr.next
            prev.next = next_node 

        return curr
    
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
    
    def size(self):
        counter = 0
        node = self.head
        while node is not None:
            counter += 1
            node = node.next
        
        return counter
    
    def search(self, value):

        node = self.head
        while node is not None:
            if node.value == value:
                return True
            else:
                node = node.next
        
        return False
    
    def index(self, item):
        counter = 0
        curr = self.head

        while curr is not None:
            if curr.value == item:
                return counter
            else:
                curr = curr.next
                counter += 1
    
    def remove(self, value):
        prev = None
        node = self.head
        
        while node is not None:
            if node.value == value:
                # change the pointer of the previous node to the next node
                if prev is None: #but need to check if it's None first
                    self.head = node.next
                else:
                    prev.next = node.next
                break
            else:
                prev = node
                node = node.next


l = List()
l.add(5)
l.add(100)
l.add(1000)

x = l.pop() # should be the value 1000
print(x.value)
print(l.size())
# print(l.size())
# print(l.index(5))
# print(l.index(100))
# print(l.index(1000))