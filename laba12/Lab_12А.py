#ВНЕШНЯЯ МНОГОФАЗНАЯ O(n logn) - во всех случаях

import heapq  # Для эффективного слияния с использованием кучи

def ext_merge_sort(arr, chunk_size):
    # Разделяем данные на чанки
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    # Сортируем каждый чанк
    for i in range(len(chunks)):
        chunks[i].sort()

    # Слияние отсортированных чанков с помощью кучи
    return list(heapq.merge(*chunks))  # heapq.merge выполняет слияние нескольких отсортированных списков

# Пример использования
seq = list(map(int, input("Введите числа через пробел: ").split()))
size = int(input("Введите размер чанка (например, 3): "))  # Размер части данных, которые помещаются в память
sorted_seq = ext_merge_sort(seq, size)
print("Отсортированная последовательность:", sorted_seq)


