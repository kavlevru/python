def bubble(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

nums = [3, 5, 99, 1, 29, 33, 14, 125, 292, 188, 56, 11]

print(bubble(nums))