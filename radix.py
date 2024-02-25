import timeit

def counting_sort(arr, position):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    
    for i in range(0, size):
        index = arr[i] // position % 10
        count[index] += 1

    
    for i in range(1, 10):
        count[i] += count[i - 1]

    
    i = size - 1
    while i >= 0:
        index = arr[i] // position % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]
    return arr

def radix_sort(arr):
    arr = arr[:]
    max_num = max(arr)
    position = 1
    while max_num // position > 0:
        rad = counting_sort(arr, position)
        position *= 10
    return rad
        
if __name__ == '__main__':
    arr = [3, 89, 67, 254, 9, 21, 185, 4, 62]
    print(radix_sort(arr))
    