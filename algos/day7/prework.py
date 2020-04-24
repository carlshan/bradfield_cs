# Following along with http://introcs.cs.luc.edu/arrays/sorting.html
import random
def shuffle(array):
    # randomly moves each element around
    for i in range(0, len(array)):
        rand_ind = random.randint(0, len(array) - 1)
        swap(array, i, rand_ind)

def swap(array, i, j):
    temp = array[j]
    array[j] = array[i]
    array[i] = temp
    return None

def bubble_sort(array):
    j = len(array) - 1
    while j > 0:
        for i in range(0, j):
            if (array[i] > array[i+1]):
                swap(array, i, i + 1)
        j -= 1


l = [19, -1, 12, 1, 5,2,3,4,5]

# swap(l, 0, 1)
bubble_sort(l)

print(l)

# Selection sort

def min_element(array, start):
    # returns index position of minimum element after start
    min_pos = start
    for i in range(start, len(array)):
        if array[i] < array[min_pos]:
            min_pos = i
    return min_pos


def selection_sort(array):
    for i in range(0, len(array)):
        min_pos = min_element(array, i)
        if min_pos != i:
            swap(array, i, min_pos)


l2 = [-5, 2, 3, -9, 100, 1]
selection_sort(l2)

print(l2)


# Insertion Sort
def insertion_sort(array):
    for j in range(1, len(array)):
        i = j
        while i > 0 and array[i] < array[i-1]:
            swap(array, i, i - 1)
            i -= 1

shuffle(l2)
print(l2)
insertion_sort(l2)
print(l2)

# Why does shell sort work better on average than insertion sort?