def sum(array):
    if array == []:
        return 0
    return array[0] + sum(array[1:])

def array_count(array):
    if array == []:
        return 0
    return 1 + array_count(array[1:])

def max(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = max(array[1:])
    return array[0] if array[0] > sub_max else sub_max

print(sum([2, 4, 6, 10, 11, 14]))