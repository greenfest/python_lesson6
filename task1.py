# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.

def getValueOfExpression(n):
    return int(n) + int(n + n) + int(n + n + n)
    
result = getValueOfExpression(input("Введите число N: "))
print(f"Значение выражения = {result}")