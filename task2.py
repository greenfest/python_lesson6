# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, 
# есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
import random

def isContaint(listNums, n):
    listNumsString = ''.join(str(x) for x in listNums)
    if (listNumsString.find(n) > -1):
        print("Найдено совпадение")
    else: print("Совпадение НЕ найдено")    

listNums = random.choices(range(9), k=15)
print(listNums)
n = input("Введите число N: ")
isContaint(listNums, n)

