import timeit
import random

from bubble import bubble_sort
from insertion import insertion_sort
from selection import selection_sort
from quick import quick_sort
from merge import merge_sort
from shell import shell_sort
from radix import radix_sort

if __name__ == '__main__':
    data_s = [random.randint(0, 1_000) for _ in range(100)]
    data_m = [random.randint(0, 10_000) for _ in range(1_000)]
    data_l = [random.randint(0, 100_000) for _ in range(10_000)]
    
    bubble_data_s = timeit.timeit(lambda: bubble_sort(data_s), number=3)
    insertion_data_s = timeit.timeit(lambda: insertion_sort(data_s), number=3)
    selection_data_s = timeit.timeit(lambda: selection_sort(data_s), number=3)
    quick_data_s = timeit.timeit(lambda: quick_sort(data_s), number=3)
    merge_data_s = timeit.timeit(lambda: merge_sort(data_s), number=3)
    shell_data_s = timeit.timeit(lambda: shell_sort(data_s), number=3)
    radix_data_s = timeit.timeit(lambda: radix_sort(data_s), number=3)
    timsort_sorted = timeit.timeit(lambda: sorted(data_s), number=3)
    timsort_sort = timeit.timeit(lambda: data_s[:].sort(), number=3)
    
    bubble_data_m = timeit.timeit(lambda: bubble_sort(data_m), number=3)
    insertion_data_m = timeit.timeit(lambda: insertion_sort(data_m), number=3)
    selection_data_m = timeit.timeit(lambda: selection_sort(data_m), number=3)
    quick_data_m = timeit.timeit(lambda: quick_sort(data_m), number=3)
    merge_data_m = timeit.timeit(lambda: merge_sort(data_m), number=3)
    shell_data_m = timeit.timeit(lambda: shell_sort(data_m), number=3)
    radix_data_m = timeit.timeit(lambda: radix_sort(data_m), number=3)
    timsort_sorted = timeit.timeit(lambda: sorted(data_m), number=3)
    timsort_sort = timeit.timeit(lambda: data_m[:].sort(), number=3)
    
    bubble_data_l = timeit.timeit(lambda: bubble_sort(data_l), number=3)
    insertion_data_l = timeit.timeit(lambda: insertion_sort(data_l), number=3)
    selection_data_l = timeit.timeit(lambda: selection_sort(data_l), number=3)
    quick_data_l = timeit.timeit(lambda: quick_sort(data_l), number=3)
    merge_data_l = timeit.timeit(lambda: merge_sort(data_l), number=3)
    shell_data_l = timeit.timeit(lambda: shell_sort(data_l), number=3)
    radix_data_l = timeit.timeit(lambda: radix_sort(data_l), number=3)
    timsort_sorted = timeit.timeit(lambda: sorted(data_l), number=3)
    timsort_sort = timeit.timeit(lambda: data_l[:].sort(), number=3)
    
   
    print(f"| {'Algorithm': <20} | {'Small': <20} | {'Medium': <20} | {'Large': <20} |")
    print(f"| {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")
    print(f"| {'Bubble sort': <20} | {bubble_data_s:20.5f} | {bubble_data_m:20.5f} | {bubble_data_l:20.5f} |")
    print(f"| {'Insertion sort': <20} | {insertion_data_s:20.5f} | {insertion_data_m:20.5f} | {insertion_data_l:20.5f} |")
    print(f"| {'Selection sort': <20} | {selection_data_s:20.5f} | {selection_data_m:20.5f} | {selection_data_l:20.5f} |")
    print(f"| {'Quick sort': <20} | {quick_data_s:20.5f} | {quick_data_m:20.5f} | {quick_data_l:20.5f} |")
    print(f"| {'Merge sort': <20} | {merge_data_s:20.5f} | {merge_data_m:20.5f} | {merge_data_l:20.5f} |")
    print(f"| {'Shell sort': <20} | {shell_data_s:20.5f} | {shell_data_m:20.5f} | {shell_data_l:20.5f} |")
    print(f"| {'Radix sort': <20} | {radix_data_s:20.5f} | {radix_data_m:20.5f} | {radix_data_l:20.5f} |")
    