"""
Homework:
1. Read over: https://my.bradfieldcs.com/algorithms/2020-04/stacks-queues-deques/
2. Answer the following questions while reading:

> 1. What is the difference between an abstract data type and an implementation of a data structure?
> 2. Consider two implementations of the queue abstract data type, one implemented using a dynamic array 
> and the other as a doubly linked list. What is the Big O complexity of the push and pop operations? 
> Other than Big O complexity, can you think of any potential performance differences between the two? 

I responded to the two questions above in Notes.md

3. Write a function that uses a stack.
4. Implement a queue using stacks instead of lists.

Along the way, I may add additional exercises for myself.
"""

# Exercise 1. Implement a stack given the following interface:

"""
* Stack() creates a new, empty stack
* .push(item) adds the given item to the top of the stack
* .pop() removes and returns the top item
* .peek() returns the top item but doesn't remove it
* .is_empty() returns whether the stack is empty
* .size() returns the number of items on the stack as an integer.
"""

class Stack(object):

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        return self._data.pop()
    
    def peek(self):
        return self._data[-1]
    
    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return len(self._data)
    
## Exercise 2.
# Prior to looking at the solution to the balanced parentheses problem, I tried to solve it using a stack.

test_pass1 = "()"
test_pass2 = "()()()"
test_pass3 = "(()(()))"
test_pass4 = "   (       ()   (abc))"
test_fail1 = "("
test_fail2 = "(()((())"
test_fail3 = "()()())"

balanced_tests = {
    'pass': [
        test_pass1,
        test_pass2,
        test_pass3,
        test_pass4,
    ],
    'fail': [
        test_fail1,
        test_fail2,
        test_fail3
    ]
}

def is_balanced(to_parse, open_symbol='(', close_symbol=')'):
    if len(to_parse) == 0:
        return True
    
    s = Stack()

    for elem in to_parse:
        if elem == open_symbol:
            s.push(elem)
        elif elem == close_symbol:
            if s.is_empty():
                return False            
            else:
                s.pop()
        else: # is not an opening or closing character, can ignore
            continue

    return s.is_empty()

def run_tests(func, tests):
    print("\n")
    print("=====Testing Passes=====")
    print("\n")
    for test in tests['pass']:
        print(test, " => ", func(test))
    print("\n")
    print("=====Testing Failures=====")
    print("\n")
    for test in tests['fail']:
        print(test, " => ", func(test))

# Exercise 3: Implement a queue before looking at the provided Bradfield implementation using stacks rather than lists

class Queue(object):
    """
    * Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
    * enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
    * dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
    * is_empty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
    * size() returns the number of items in the queue. It needs no parameters and returns an integer.
    """

    def __init__(self):
        self._items = Stack()

    def enqueue(self, item):
        self._items.push(item)

    def dequeue(self):
        """
            Creates a new Stack as a temporary placeholder
            Loop over the ._items Stack until I reach the end
                If I haven't reached the end, put the item in the loop into the new Stack

            Once I've reached the end, pop this final element and store it in a variable that will be returned
            Reverse the placeholder Stack to recover the original order of the ._items stack

            Performance analysis:
                Time: O(N) <- needs to go through all N elements twice: once to get the element at the bottom of the stack, and another to reverse the temporary stack to recover the origina order (well, N-1 the second time)

                Space: Needs to create a temporary stack of N elements.
                    Question: is there a way to reverse in place so that I don't use another temporary stack?
        """

        new_items = Stack()
        while not self._items.is_empty():
            curr = self._items.pop()
            new_items.push(curr)
        
        last = new_items.pop()

        # need to reverse new_items before pushing it back onto the original stack
        while not new_items.is_empty():
            item = new_items.pop()
            self._items.push(item)

        return last 

    def is_empty(self):
        return self._items.is_empty()
    
    def size(self):
        return len(self._items)
        
# q = Queue()
# q.enqueue(5)
# q.enqueue('abc')
# q.enqueue(12345)
# q.enqueue('apple')

# while not q.is_empty():
#    print(q.dequeue())

# Exercise 4. Implement a Deque
class Dequeue(object):
    """
    * Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
    * add_front(item) adds a new item to the front of the deque. It needs the item and returns nothing.
    * add_rear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
    * remove_front() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
    * remove_rear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
    * is_empty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
    * size() returns the number of items in the deque. It needs no parameters and returns an integer.
    """

    def __init__(self):
        self._items = []
    
    def add_front(self, item):
        self._items.insert(0, item)
    
    def add_rear(self, item):
        self._items.append(item)
    
    def remove_front(self):
        return self._items.pop(0)

    def remove_rear(self):
        return self._items.pop()
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)

# Exercise 5. Use the above implementation of a Dequeue to create a palindrome checker, before looking at the provided Bradfield implementation

palindrome_tests = {
    "pass":[
        "racecar",
        "madam",
        "aabbaa",
        "a",
        ""
    ],
    "fail": [
        "ab",
        "racecars"
    ]
}

def check_palindrome(string):

    d = Dequeue()
    tokens = list(string.lower().replace(' ', ''))

    for token in tokens:
        d.add_rear(token) 
    
    for token in tokens:
        to_compare = d.remove_rear() # compare the original order with the reverse order
        if token != to_compare:
            return False

    return True
    



if __name__ == "__main__":
    should_run_tests = True 
    if should_run_tests:
        run_tests(is_balanced, balanced_tests)
        run_tests(check_palindrome, palindrome_tests)
