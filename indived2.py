# -*- coding: utf-8 -*-
import sys
import math

if __name__ == '__main__':
    A = list(map(float, input("Введите список:").split()))
    i = 0
    C = int(input("Введите С:"))
    for item in A:
        if item < C:
            i += 1
    print(f"Колличество элеменнтов больше веденного числа = {C}")
    t = 0
    for item in A:
        if item > 0:
            cel = int(math.floor(item))
            t += cel
        else:
            t = 0
    print(f"Сумма элементов после последнего отрицательного элемента списка = {t}")
    list_2 = []
    list_3 = []
    q = max(A)
    for item in A:
        if q + (q * 0.2) >= item >= q - (q * 0.2):
            list_2.append(item)
        else:
            list_3.append(item)
    list_sum = list_2 + list_3
    print(list_sum)
