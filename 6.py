"""
Был реализован алгоритм экспоненциального фильтра. 

Инициализируем массив измерений

После этого проходим по всем полученным измерениям и применяем формулу. 
Полученные значения записываем в массив s для дальнейшего вывода на экран.
"""

import random
from random import randint

arr = [random.randint(0, 100) for i in range(20)]

print(arr)

def expFilter(arr, alpha):
    s = [arr[0]]
    for i in range(1, len(arr)):
        s.append(s[i-1] + alpha * (arr[i] - s[i-1]))
    return s

print(expFilter(arr, 0.5))