# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
N = int(input("Введите N = "))
X = int(input("Введите X = "))
Q = int(input("Введите максимальное значение Q = "))
s = 0
h = 0
m = 0
arr = [random.randint(1,Q) for _ in range(N)]
print(arr)
for i in arr:
    # print(i)
    if X < i:
        s = i
    if X > i:
        h = i
    elif X == i:
        m = i
# print(f"H = {h}")
# print(f"S = {s}")
for l in arr:
    if l < X and l > h:
        h = l
        print(f"5 = {h}")
    if l > X and l < s:
        s = l
    if l == X:
        m = l
print(f"H = {h}")
print(f"S = {s}")
print(f"M = {m}")
if X == m:
    print(f'Ближайшее число Х равно {m}')
    exit(0)
if  X - h > s - X:
    print(f'Ближайшее число Х равно {s}')
    exit(0)
if  X - h < s - X:
    print(f'Ближайшее число Х равно {h}')
    exit(0)