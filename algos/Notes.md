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

A list is not the same as a Python list (which should better be called as an array). Rather it holds references to the next node and previous node in a list.

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

### Homework Questions

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

Implementing a queue using a doubly-linked list:

* .push() -> O(N) as we need to traverse the list to find the last element to push onto
* .pop() -> O(N) as we need to traverse the list to get to the end
* .dequeue -> O(1) as we just need to update the pointer of head to the new node, and have the new node point to the previous head, and update the previous head to have a link to the new head. We don't need to touch any of the remaining nodes.

## [Hashing](https://bradfieldcs.com/algos/searching/hashing/)

Hashing is a concept that, among other things, allows us to search a data structure in `O(1)` constant time. A **hash table**. is a collection of items that is organized in such a way where there are "slots" with "names". A special way of assigning values to slots is done through a "hash function" `H(value)`.

When you want to access a value in the hash table, simply compute `H(value)` and that will return the correct "name" or "address" of the item, allowing you to retreive it without regard for e.g., the size of the hash table.

Intended ideal behavior of the hash function:

* 1-1 mapping between input values and resulting outputs. No two inputs should map to the same output and each input should map to only one output.
* It returns the address of a specific slot in our hash table (this is where module arithmetic will help).

There are a few different ways to construct a hash function that behaves the way we want:

1. *Folding method:* Divide your data into chunks, add up the results and `mod` the result by the size of your hash table to figure out the correct address. E.g., the phone number `436-555-4601` can get broken up into `(43, 65, 55, 46, 01)` which can be summed and modded.
2. *Mid-square method:* Square the value, then extract some portion of the remainnig digits, followed by modding it.
3. *Treating characters as numbers*: `sum(ord(c) for c in string)` can be hashed.

### What happens if there are collisions?

There are some strategies to resolve hash collisions. One is called *linear probing.* Essentially, if a collision occurs the technique looks at the nearby values for the next open slot. However, this strategy may produce clustering of values and subsequent lookups of values that have collisions will also require linear search.

There is also *quadratic probing* where the number of slots skipped increases quadratically.

Another method for handling collisions is to allow each slot to hold a reference to another set of values, such as a linked list.

**Cuckoo Hashing**
Yet another way is to implement [Cuckoo hashing](https://blog.bradfieldcs.com/an-introduction-to-hashing-in-the-era-of-machine-learning-6039394549b0). Essentially, this technique maintains two hash functions for two different memory addresses: call them `primary` and `secondary` functions for the corresponding addresses.

In the beginning, use the `primary` hash function to hash to the primary allocated addresses. If there is a collision, evict the current value and replace it with the new one. Now hash the evicted value with the `secondary` function to the new address space.

## [Priority Queues with Binary Heaps](https://bradfieldcs.com/algos/trees/priority-queues-with-binary-heaps/)

A priority queue is similar to a queue, with the main exception being that the logical order of items inside is queue is determined by their "priority."

One way to implement it is to use a data structure called a `binary heap`, which will allow enqueue and dequeue operations to take `O(logn)` time. A `binary heap` has two variations: **min heap** and **max heap.** The difference between them is where the *key* is located. In a **min heap** the smallest key is always at the front. Whereas in a **max heap** the largest key is located in the front.

### Structure of a Binary Heap

In order for the heap to be efficient, it needs to be "balanced" in that the there should roughly be the same number of nodes in the left and right subtrees.

## Dynamic Programming

What is dynamic programming?

DP describes a problem-solving technique that is best applied to problems where there are overlapping sub-problems, oftentimes with a recursive structure.

The advantage of using DP instead of recursive techniques is that they may oftentimes be much more efficient in both time and space.

The key steps for solving a problem using dynamic programming are the following:

1. Define the subproblems
2. Write down the recurrence that relates the subproblems
3. Recognize and solve the base cases.

Let's apply the above three steps in an example:

**Problem:** Given `n`, find the number of different ways to write `n` as the sum of `1`, `3`, and `4`.

Example: for `n=5`, the answer is `6`:

```python
5 = 1 + 1 + 1 + 1 + 1
  = 1 + 1 + 3
  = 1 + 3 + 1
  = 3 + 1 + 1
  = 1 + 4
  = 4 + 1
```

Let's apply each of the DP steps one-by-one:

### Step 1: Define the Subproblems

- Let $D_n$ be the number of ways to write `n` as the sum of `1`, `3`, and `4`.
- Let one possible solution be $n = x_1 + x_2 + ... + x_m$
- Consider if $x_m = 1$ then the rest of the terms must sum to $n-1$

### Step 2: Find the recurrence

- Therefore the number of sums that end with $x_m$ is $D_{n-1}$
- Now, apply the same reasoning to the other possible numbers `3` and `4`.
- The recursive structure is therefore $D_n = D_{n-1} + D_{n-3} + D_{n-4}$.

### Step 3: Recognize and solve the base cases

- If $n < 0$ then $D_n=0$
- If $n=0$ then $D_n=1$
- If $n=1$ then $D_n=1$
- If $n=2$ then $D_n=1$
- If $n=3$ then $D_n=2$

So in pseudo-code then:

```javascript
D[0] = D[1] = D[2] = 1; D[3] = 2

for (i = 4; i <= n; i ++) {
    D[i] = D[i-1] + D[i-3] + D[i-4];
}
```

Note that the above solution takes into account the recursive recurrence structure but does not implement a recursive solution.

## [Binary Search](https://bradfieldcs.com/algos/searching/the-binary-search/)

If a list is ordered, we do not need to search in sequential $O(N)$ time, but rather search in $O(\log_{2}N)$ time.

We can achieve this by doing something called binary search. The way it works:

1. Start by examining the middle item.
2. If that item is not correct, we can eliminate half of the remaining items.
3. Repeat this by examining the middle of the remaining half.

### Homework

1. Hashing and binary search both address the same problem: finding an item in a collection. What are some trade-offs between the two strategies? When might you want to pick one over the other?
2. If sorting takes (at minimum) $O(n\log_{2} n)$ time, and binary search takes $O(\log_{2} n)$ time, under what circumstances might it worth it to sort a collection in order to perform binary search?

**Responses:**

1. Some comparisons and contrasts between hashing and binary seaching:
   * With hashing, you can lookup objects that don't have some natural "ordering" like numbers do, whereas for binary search to work there needs to be some definition of an "order" so that you compare "greater" or "less than."
   * If the cost of sorting $N$ items is heavier than just hashing all items, you may just want to go with hashing.
   * Vice versa. If it is computationally expensive to hash certain items (maybe long strings?) then sorting may be better.
   * For binary search, once you've sorted you can use it for other purposes and build other data structures that may rely on sorted data.
   * If you sort in place, you don't use additional memory, unlike with hashing.
2. If we expect to amortize the cost of $O(nlog_{2}n)$ sort over many fast $O(log_{2}n)$ searches, we may be okay sorting the collection in order to perform binary search. Similarly if future tasks may require sorting the data.

## [Divide and Conquer](https://my.bradfieldcs.com/algorithms/2020-04/divide-and-conquer/)

This week will focus primarily on how to use divide and conquer strategies in the context of sorting.

### Bubble Sort

Bubble sort works by scanning through the array, exchanging adjascent items that are out of order.

Casually speaking, the algorithm can be described as follows:

1. Loop through your array starting from the end. Call the current loop iteration $j$.
2. In each loop, loop through the beginning until the $j$th element.
3. In this inner loop, check to see if neighboring elements are in the correct order. If not, swap them.