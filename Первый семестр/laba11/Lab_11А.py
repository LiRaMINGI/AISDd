#БЫСТРАЯ O(n logn) - в лучшем и среднем случае; О(n^2) - в худшем случае

def qsort(arr):
    if len(arr) <= 1:  # Базовый случай
        return arr

    piv = arr[1]  # Опорный элемент
    l = [x for x in arr[:-1] if x < piv]  # Меньшие или равные опорному
    r = [x for x in arr[:-1] if x >= piv]  # Больше опорного

    # Рекурсивно сортируем и объединяем
    return qsort(l) + [piv] + qsort(r)

arr = [12, 34, 814, 54, 2, 3, 180, 97, 8]
print("Исходный массив:", arr)

qsort(arr)

print("Отсортированный массив:", arr)
