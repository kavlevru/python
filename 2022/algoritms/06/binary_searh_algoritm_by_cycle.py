def binary_search(array, item):
    low = 0
    high = len(array) - 1
    count = 0
    while low < high:
        mid = (low + high) // 2
        guess = array[mid]
        print(array[low:high + 1])
        count += 1
        if guess == item:
            print("Count: {count}".format(count=count))
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


array = [1, 3, 5, 99, 180, 188, 295, 344, 456, 569, 998]

print(binary_search(array, 1))