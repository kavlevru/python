def euclidian_algoritm(num1, num2):
    return num1 if num2 == 0 else euclidian_algoritm(num2, num1 % num2)

print(euclidian_algoritm(1368, 768))