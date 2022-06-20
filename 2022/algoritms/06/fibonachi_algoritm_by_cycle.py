def fibonachi(steps):
    f1 = f2 = 1
    i = 0
    array = []
    while i < steps:
        f1, f2 = f2, f1 + f2
        array.append(f1)
        i += 1
    return array
steps = 50
print(fibonachi(steps))