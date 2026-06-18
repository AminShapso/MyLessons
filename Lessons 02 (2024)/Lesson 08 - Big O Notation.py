"""
Time complexity is a way of expressing how the runtime of a function grows as the input size increases.
It's often expressed using Big O notation.
"""


import itertools


def constant_time_example(arr):
    """
    O(1) - Constant Time
    Accessing a specific element in an array takes constant time,
    regardless of the size of the array.
    """
    return arr[0]  # Accessing the first element in the list


def bubble_sort(arr):
    """
    O(n^2) - Bubble Sort
    Repeatedly swaps adjacent elements if they are in wrong order.
    """
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """
    O(n^2) - Selection Sort
    Selects the smallest element and moves it to the front.
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    """
    O(n^2) - Insertion Sort
    Builds sorted array one element at a time.
    Good for nearly sorted data.
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def linear_time_example(arr):
    """
    O(n) - Linear Time
    The algorithm iterates through each element in the array once,
    so the time taken grows linearly with the size of the input list.
    """
    arr_out = []
    for item in arr:
        arr_out.append(item)
    return arr_out


def quadratic_time_example(arr):
    """
    O(n^2) - Quadratic Time
    This occurs when there are nested loops.
    """
    arr_out = []
    for i in arr:
        for j in arr:
            arr_out.append((i, j))  # Nested loop prints all pairs (i, j)
    return arr_out


def binary_search(arr, target):
    """
    O(log n) - Logarithmic Time
    The binary search algorithm repeatedly divides the input array in half,
    reducing the problem size by half at each step.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def merge_sort(arr):
    """
    O(n log n) - Linearithmic Time
    Merge sort divides the array in half recursively, then merges the sorted halves.
    Each division takes log(n) time and merging takes linear time.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def fibonacci(n):
    """
    O(2^n) - Exponential Time
    The naive recursive solution to the Fibonacci sequence calls the function twice for each number,
    leading to an exponential growth in the number of function calls.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def generate_permutations(arr):
    """
    O(n!) - Factorial Time
    Generating all permutations of an array has factorial time complexity, 
    because the number of permutations of an array of size n is n!.
    """
    return list(itertools.permutations(arr))


def merge_lists(list1, list2):
    """
    O(n + m) - Linear Time with Two Inputs
    The time complexity here is the sum of the lengths of both lists because we iterate through both lists once.
    Important nuance: it creates a new list (copying elements)
    """
    result = list1 + list2
    return result


if __name__ == '__main__':
    print("O(1) Example: Constant Time")
    arr1 = [10, 30, 20]
    print(constant_time_example(arr1))  # O(1)

    print("\nO(n) Example: Linear Time")
    print(linear_time_example(arr1))  # O(n)

    print("\nO(n^2) Example 01: Quadratic Time")
    print(quadratic_time_example(arr1))  # O(n^2)

    print("\nO(n^2) Example 02: Bubble Sort")
    print(bubble_sort(arr1))  # O(n^2)

    print("\nO(n^2) Example 03: Selection Sort")
    print(selection_sort(arr1))  # O(n^2)

    print("\nO(n^2) Example 04: Insertion Sort")
    print(insertion_sort(arr1))  # O(n^2)

    print("\nO(log n) Example: Logarithmic Time")
    arr2 = [1, 3, 5, 7, 9, 11, 13, 15]  # Sorted array
    print(binary_search(arr2, 7))  # O(log n)

    print("\nO(n log n) Example: Merge Sort (Linearithmic Time)")
    arr3 = [5, 2, 9, 1, 5, 6]
    print(merge_sort(arr3))  # O(n log n)

    print("\nO(2^n) Example: Exponential Time (actually  1.618^n, but commonly approximated that way in interviews)")
    print(fibonacci(6))  # O(2^n)

    print("\nO(n!) Example: Factorial Time")
    arr4 = [1, 2, 3]
    print(generate_permutations(arr4))  # O(n!)

    print("\nO(n + m) Example: Linear Time with Two Inputs")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(merge_lists(list1, list2))  # O(n + m)
