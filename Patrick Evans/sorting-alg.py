"""
ARRAY USED:
[5.8, 16, 10, 3, 1, 4]

--------------------------------------------------
BUBBLE SORT
Running Time:
Best Case: O(n)        -> already sorted
Average Case: O(n^2)
Worst Case: O(n^2)
--------------------------------------------------
"""

arr = [5.8, 16, 10, 3, 1, 4]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


"""
--------------------------------------------------
SELECTION SORT
Running Time:
Best Case: O(n^2)
Average Case: O(n^2)
Worst Case: O(n^2)
--------------------------------------------------
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


"""
--------------------------------------------------
INSERTION SORT
Running Time:
Best Case: O(n)        -> already sorted
Average Case: O(n^2)
Worst Case: O(n^2)     -> reverse order
--------------------------------------------------
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


"""
--------------------------------------------------
MERGE SORT
Running Time:
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)
--------------------------------------------------
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


"""
--------------------------------------------------
QUICK SORT
Running Time:
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n^2)     -> poor pivot choice
--------------------------------------------------
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


# ------------------ OUTPUT ------------------

print("Original Array:", arr)

print("Bubble Sort:", bubble_sort(arr.copy()))
print("Selection Sort:", selection_sort(arr.copy()))
print("Insertion Sort:", insertion_sort(arr.copy()))
print("Merge Sort:", merge_sort(arr.copy()))
print("Quick Sort:", quick_sort(arr.copy()))
