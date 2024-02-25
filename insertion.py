import timeit

def insertion_sort(lst_):
    lst = lst_[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

if __name__ == '__main__':
    numbers1 = [5, 13, 20, 0, 1, 9, 4, 8, 2, -1, 6, 11, -2, 22, 33, 44, 7, 12.0, 14.8]
    numbers2 = [2, 4, 6, 1]
    print(insertion_sort(numbers1))
    print(insertion_sort(numbers2))