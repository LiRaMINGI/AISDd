from typing import List

def backtrack(weights: List[int], capacity: int, start: int, bins: List[int], min_bins: int) -> tuple[List[int], int]:
    """
    Рекурсивная функция для поиска оптимального решения задачи bin packing методом backtracking.

    Аргументы:
        weights (List[int]): Список весов предметов.
        capacity (int): Вместимость одного контейнера.
        start (int): Индекс текущего предмета для размещения.
        bins (List[int]): Текущее распределение весов по контейнерам (хранятся остатки свободного места).
        min_bins (int): Текущий минимальный найденный размер контейнеров.

    Возвращает:
        tuple[List[int], int]: Обновлённое состояние bins и обновлённое значение min_bins.
    """
    # Если все предметы размещены — проверяем, нашли ли мы лучшее решение
    if start == len(weights):
        min_bins = min(min_bins, len(bins))
        return bins, min_bins

    # Пробуем положить текущий предмет в один из уже существующих контейнеров
    for i in range(len(bins)):
        if bins[i] + weights[start] <= capacity:
            bins[i] += weights[start]  # Помещаем предмет
            bins, min_bins = backtrack(weights, capacity, start + 1, bins, min_bins)
            bins[i] -= weights[start]  # Откатываем изменение

    # Если не удалось разместить в существующих — создаём новый контейнер
    bins.append(weights[start])
    bins, min_bins = backtrack(weights, capacity, start + 1, bins, min_bins)
    bins.pop()  # Откатываем добавление нового контейнера

    return bins, min_bins


def bin_packing_subset(weights: List[int], capacity: int) -> int:
    """
    Основная функция для решения задачи упаковки в контейнеры (bin packing).

    Цель: минимизировать количество контейнеров, необходимых для упаковки всех предметов,
    при условии, что суммарный вес в каждом контейнере не превышает capacity.

    Аргументы:
        weights (List[int]): Список весов предметов.
        capacity (int): Вместимость одного контейнера.

    Возвращает:
        int: Минимальное количество контейнеров, необходимое для упаковки всех предметов.
    """
    min_bins = float("inf")
    bins = []
    _, min_bins = backtrack(weights, capacity, 0, bins, min_bins)
    return min_bins


if __name__ == "__main__":
    # Тестовый пример
    print(bin_packing_subset([4, 5, 2, 1, 3], 6))  # Ожидается: 3