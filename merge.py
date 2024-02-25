import timeit

def merge_sort(arr):
    arr = arr[:]
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

if __name__ == '__main__':
    numbers1 = [5, 13, 20, 0, 1, 9, 4, 8, 2 , 1, -1, 6, 11, -2, 22, 33, 44, 7, 12.0, 14.8]
    numbers2 = [2, 4, 6, 1, 12, 0, -1]
    print(merge_sort(numbers1))
    print(merge_sort(numbers2))
    