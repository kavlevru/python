def find_smallest_index(array):
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < array[smallest_index]:
            smallest_index = i
    return smallest_index

def selection_sort(array):
    sorting_array = []
    for i in range(len(array)):
        smallest = find_smallest_index(array)
        sorting_array.append(array.pop(smallest))
    return sorting_array

array = [15, 12, 188, 96, 325, 14, 14, 22, 29, 39]

print(selection_sort(array))