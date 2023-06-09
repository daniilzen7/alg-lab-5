"""
инициализируем набор из элементов массива. После чего, находим минимальное число в списке и записываем его в index.
Проходим по словарю и проверяем, есть ли индекс в нем. Если да, то увеличиваем индекс на 1,
иначе получаем искомое значение и выводим его.
"""

# Функция поиска наименьшего пропущенного положительного числа в несортированном массиве
def findSmallestMissing(nums):
 
    # инициализирует набор из элементов массива
    distinct = {*nums}
 
    # возвращает первое наименьшее отсутствующее положительное число из набора
    index = min(nums)
    while True:
        if index not in distinct:
            return index
        index += 1
 
 
nums = [1, 4, 2, -1, 6, 5]
print('Самое маленькое пропущенное число:',
        findSmallestMissing(nums))