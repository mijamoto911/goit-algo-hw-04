import timeit

def quick_sort(arr):
    if len(arr)<= 1:
        return arr
    pivot = arr[len(arr)// 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    numbers1 = [5, 13, 20, 0, 1, 9, 4, 8, 2 , 1, -1, 6, 11, -2, 22, 33, 44, 7, 12.0, 14.8]
    numbers2 = [2, 4, 6, 1, 12, 0, -1]
    print(quick_sort(numbers1))
    print(quick_sort(numbers2))