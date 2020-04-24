# Mergesort

def interleave(l1, l2, counter):
    result = []

    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            counter += 1
            result.append(l2[j])
            j += 1

    while i < len(l1):
        result.append(l1[i])
        i += 1
    while j < len(l2):
        result.append(l2[j])
        j += 1

    return result, counter

def mergesort(array, counter):
    # TODO: Doesn't work just yet.
    # See: [2, 10, -1, 100]
    """
        parameters:
            array: list
            counter: int

        returns:
            sorted_arr: list
                sorted version of array
            counter: int
                the total number of inversions in the array
    """
    if len(array) <= 1:
        return array, 0
    else:
        midpoint = len(array) // 2
        left, left_count = mergesort(array[:midpoint], counter)
        right, right_count = mergesort(array[midpoint:], counter)

        # interleave them together and count the number of inversions
        # necessary to interleave.
        sorted_arr, final_count = interleave(left, right, left_count + right_count)

        return sorted_arr, final_count

def count_inversions(l):
    sorted_arr, counter = mergesort(l, 0)
    return sorted_arr, counter

test_arr = [2, 10, -1, 100] # 2 inversions
sorted_arr, counter = count_inversions(test_arr)
print(test_arr, "has", counter, "inversions.")

test_arr = [2, 10, 100] # 0 inversions
sorted_arr, counter = count_inversions(test_arr)
print(test_arr, "has", counter, "inversions.")

test_arr = [10, 1, 100] # 1 inversions
sorted_arr, counter = count_inversions(test_arr)
print(test_arr, "has", counter, "inversions.")

test_arr = [1000, 10, 1, 100] # 4 inversions
sorted_arr, counter = count_inversions(test_arr)
print(test_arr, "has", counter, "inversions.")

test_arr = [1000, 0, 10, -2, 1, 100] # 5 inversions
sorted_arr, counter = count_inversions(test_arr)
print(test_arr, "has", counter, "inversions.")

test_arr = [1, 10, 100, 0, 5, 1000] # 5 inversions
sorted_arr, counter = count_inversions(test_arr)
print(test_arr, "has", counter, "inversions.")