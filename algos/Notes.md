# Notes on Algorithms and Data Structures

The below are notes from reading the various sections on [Bradfield's online algorithms introduction](https://bradfieldcs.com/algos/stacks/introduction/).

## Stacks

Stacks are one type of linear data structure. The others that we'll be learning about include queues, deques and lists. These data structures are called linear because when items are added to it, the position of this new item stays the same relative to its neighbors.

What distinguishes linear data structures from one another is where additions and removals of items happen.

A "stack" evokes a stack of e.g., books or plates. That metaphor is helpful for remembering the key property of stacks that distinguishes it from other linear data structures: removals and additions happen on the same end, and only on that end. That end is typically called "the top" of the stack. Newer items are put "on top" of the stack, so as you go down (or "deeper") into the stack, you reach older items.

As a result, we reach one of the key features of a stack: the insertion order is the opposite of the removal order. 

The key methods a stack has are:

* Stack() creates a new, empty stack
* .push(item) adds the given item to the top of the stack
* .pop() removes and returns the top item
* .peek() returns the top item but doesn't remove it
* .is_empty() returns whether the stack is empty
* .size() returns the number of items on the stack as an integer.

### What are some clues that we should use a Stack data structure to solve a problem?
When processing a sequence of data and there is some sense of one element needs to interact with the first subsequent element that meets a condition (e.g., an opening parenthesis that needs a closing paranthesis).

## Queues

A queue is a linear data structure where addition happens at one end, but removals happen at the other. Think of a line at a checkout counter at a grocery store. Additions to the line happen at "the rear" and those who are checked out leave "the front."

Queues are used in problems where a "FIFO" or "first-in first-out" approach needs to be observed (e.g., queuing a series of instructions to run).

The key methods to a queue are:

* Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
* enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
* dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
* is_empty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
* size() returns the number of items in the queue. It needs no parameters and returns an integer.

### What are some clues that we should use a Queue data structure?
When there's some circularity, where the person at the front of the line goes to the back.
When we need to process data from the earliest to the last. 

## Dequeues
Deques can be modified from both the rear and the front by both dding and removing items.

It is called a "deque" as it is a double-ended queue.

The key methods to a deque are:

* Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
* add_front(item) adds a new item to the front of the deque. It needs the item and returns nothing.
* add_rear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
* remove_front() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
* remove_rear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
* is_empty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
* size() returns the number of items in the deque. It needs no parameters and returns an integer.

## Lists
A list is not the same as a Python list (which should better be called as an array). Rather it cannot hold duplicate items and can hold references to the next node and previous node in a list.

A list where each of the nodes holds only a reference to the next node is called singly-linked. A node that holds both references to the next and previous nodes are called "doubly-linked".

The key methods to a list are:

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

### Homework Questions:
In consider all of the data structures we've learned, answer the following two questions:

> 1. What is the difference between an abstract data type and an implementation of a data structure?
> 
> 2. Consider two implementations of the queue abstract data type, one implemented using a dynamic array 
> and the other as a doubly linked list. What is the Big O complexity of the push and pop operations? 
> Other than Big O complexity, can you think of any potential performance differences between the two? 


**Question 1.**

The difference between an abstract data type (ADT) and an implementation is similar to the difference between a blueprint for a building, and the actual building. Or between a language specification (e.g., Python) and the particular choice of implementation for that specification (e.g., CPython, PyPy, IronPython).

One describes the key logical properties of the system. And the other is the actual derived implementation of this description. 

The ADT is the abstraction that, during system design, allows problem-solvers to consider solutions independent of a particular implementation. 


**Question 2.**
Implementing a queue using an array:
* .push() -> O(1) as we only need to put the new item at the end
* .pop() -> O(1) as we only need the last item
* .dequeue() -> O(N) as we need to delete the first element, but then copy all of the original elements over by one

Implementing using a doubly-linked list:
* .push() -> O(N) as we need to traverse the list to find the last element to push onto
* .pop() -> O(N) as we need to traverse the list to get to the end 
* .dequeue -> O(1) as we just need to update the pointer of head to the new node, and have the new node point to the previous head, and update the previous head to have a link to the new head. We don't need to touch any of the remaining nodes.