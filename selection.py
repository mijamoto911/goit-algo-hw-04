import timeit

def selection_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__':
    numbers1 = [5, 13, 20, 0, 1, 9, 4, 8, 2 , 1, -1, 6, 11, -2, 22, 33, 44, 7, 12.0, 14.8]
    numbers2 = [2, 4, 6, 1]
    print(selection_sort(numbers1))
    print(selection_sort(numbers2))