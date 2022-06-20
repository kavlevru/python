def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest_index(array)
        new_array.append(array.pop(smallest))
    return new_array

def find_smallest_index(array):
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < array[smallest_index]:
            smallest_index = i
    return smallest_index

array = [10, 9, 5 , 8, 6, 7]

print(selection_sort(array))