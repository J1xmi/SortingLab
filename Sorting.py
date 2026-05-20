import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])
    return _merge_blocks(left_part, right_part)

def _merge_blocks(left, right):
    sorted_arr = []
    pointer_l = pointer_r = 0
    while pointer_l < len(left) and pointer_r < len(right):
        if left[pointer_l] <= right[pointer_r]:
            sorted_arr.append(left[pointer_l])
            pointer_l += 1
        else:
            sorted_arr.append(right[pointer_r])
            pointer_r += 1
    sorted_arr.extend(left[pointer_l:])
    sorted_arr.extend(right[pointer_r:])
    return sorted_arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    elements = arr.copy()
    _quicksort_helper(elements, 0, len(elements) - 1)
    return elements

def _quicksort_helper(arr, low, high):
    if low < high:
        pivot_idx = _partition(arr, low, high)
        _quicksort_helper(arr, low, pivot_idx - 1)
        _quicksort_helper(arr, pivot_idx + 1, high)

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def run_lab_requirements():
    print("Timing of 10,000 elements")
    data_10k = [random.randint(0, 100000) for _ in range(10000)]
    s1 = time.time()
    merge_sort(data_10k.copy())
    print(f"MergeSort (10k): {time.time() - s1:.4f} сек")
    s2 = time.time()
    quick_sort(data_10k.copy())
    print(f"QuickSort (10k): {time.time() - s2:.4f} сек")

if __name__ == "__main__":
    run_lab_requirements()
  
