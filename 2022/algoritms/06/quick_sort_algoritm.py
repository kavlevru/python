def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] #10
        less = [i for i in array[1:] if i <= pivot] #5.2.3
        print(less)
        greater = [i for i in array[1:] if i > pivot] #[] #[] #[]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 10, 5, 3, 2, 2]))