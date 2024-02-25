import timeit

def bubble_sort(lst_):
    lst = lst_.copy()
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

if __name__ == '__main__':
    numbers1 = [5, 13, 20, 0, 1, 9, 4, 8, 2 , 1, -1, 6, 11, -2, 22, 33, 44, 7, 12.0, 14.8]
    numbers2 = [2, 4, 6, 1]
    print(bubble_sort(numbers1))
    print(bubble_sort(numbers2))
    
