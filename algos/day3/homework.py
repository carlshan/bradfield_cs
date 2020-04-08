"""
Homework:
1. Read about Hashing: https://bradfieldcs.com/algos/searching/hashing/
2. Read about Priority Queues using Binary Heaps: https://bradfieldcs.com/algos/trees/priority-queues-with-binary-heaps/
3. Implement a binary heap

"""

class BinaryHeap(object):
    """
    BinaryHeap() creates a new, empty, binary heap.
    insert(k) adds a new item to the heap.
    find_min() returns the item with the minimum key value, leaving item in the heap.
    del_min() returns the item with the minimum key value, removing the item from the heap.
    is_empty() returns true if the heap is empty, false otherwise.
    size() returns the number of items in the heap.
    build_heap(list) builds a new heap from a list of keys.

    """

    def __init__(self):
        self.items = [0] # initializing with 0 to allow for integer division later on

    def __len__(self):
        return len(self.items) - 1 # minus 1 to account for the initial 0
    
    def percolate_up(self):
        # swaps items with parents until complete
        i = len(self)

        while i // 2 > 0: # same as i > 1
            parent_ind = i // 2
            if self.items[i] > self.items[parent_ind]:
                # swap the two
                self.items[i], self.items[parent_ind] = self.items[parent_ind], self.items[i]
            
            i = parent_ind

    def insert(self, item):
        # check the value of the item with it's parent and until it is larger than it's parent
        self.items.append(item)
        self.percolate_up() 
    
    def size(self):
        return len(self.items) - 1 

    def is_empty(self):
        return len(self.items) == 1

    def find_min(self):
        # finds the minimum value of the tree, which should be at position 1 in self.items
        return self.items[1]
    
    def percolate_down(self, i):
        # i is the depth of the tree (with the top being i=1) that you are percolating down from
        # swap the root with it's smallest child less than the root
        # repeat this swapping process until the node is swapped onto a position on the tree where it is already less
        # than both children
        while i * 2 <= len(self):

            smallest_child_ind = self.min_child(i)
            if self.items[i] > self.items[smallest_child_ind]:
                self.items[i], self.items[smallest_child_ind] = self.items[smallest_child_ind], self.items[i]
            
            i = smallest_child_ind

    def min_child(self, i):
        furthest_child_location = i * 2 + 1
        nearest_child_location = i * 2

        if furthest_child_location > len(self): # furthest child does not exist
            return nearest_child_location 
        
        if self.items[nearest_child_location] < self.items[furthest_child_location]:
            return nearest_child_location
        else:
            return furthest_child_location
        
    
    def delete_min(self):
        # first, it swaps the minimum with the last item in the list
        # then it percolates down the list
        to_return = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self.percolate_down(1)

        return to_return