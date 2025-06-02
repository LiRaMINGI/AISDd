import sys
from typing import List, Tuple

def tsp_with_path(dist: List[List[int]], start: int) -> Tuple[int, List[int]]:
    """
    Решает задачу коммивояжёра (TSP) методом динамического программирования с битовыми масками.

    Алгоритм:
    - Используется DP[mask][i] — минимальная стоимость пути, посетившего города из mask и закончившегося в i.
    - mask — это битовая маска, где установленные биты соответствуют посещённым городам.
    - Восстанавливается оптимальный путь через массив parent.

    Аргументы:
        dist (List[List[int]]): Матрица расстояний между городами (n x n), где dist[i][j] — стоимость перехода из i в j.
        start (int): Начальный город (индекс).

    Возвращает:
        Tuple[int, List[int]]: 
            - Общая минимальная стоимость замкнутого маршрута.
            - Список индексов городов в порядке обхода (включает возврат в начальный город).
    """
    n = len(dist)
    total_mask = (1 << n) - 1  # Все города посещены

    # dp[mask][i] — минимальная стоимость пути, при котором посещены города из mask и мы стоим в i
    dp = [[sys.maxsize] * n for _ in range(total_mask + 1)]
    dp[1 << start][start] = 0  # Начальное состояние: стоим в start, посетили только его

    # parent[mask][i] — предыдущий город перед i в состоянии mask
    parent = [[-1] * n for _ in range(total_mask + 1)]

    # Заполняем dp для всех масок
    for mask in range(total_mask + 1):
        for i in range(n):
            if not (mask & (1 << i)):  # Если i не в маске — пропускаем
                continue

            for j in range(n):
                if mask & (1 << j):  # Если j уже посещён — пропускаем
                    continue

                new_mask = mask | (1 << j)  # Добавляем j в маску
                if dp[mask][i] + dist[i][j] < dp[new_mask][j]:
                    dp[new_mask][j] = dp[mask][i] + dist[i][j]
                    parent[new_mask][j] = i  # Сохраняем предка

    # Находим минимальную стоимость завершения цикла
    min_cost = sys.maxsize
    last_city = -1
    for i in range(n):
        if i == start:
            continue
        cost_with_return = dp[total_mask][i] + dist[i][start]
        if dp[total_mask][i] != sys.maxsize and cost_with_return < min_cost:
            min_cost = cost_with_return
            last_city = i

    # Восстановление пути
    path = []
    mask = total_mask
    current = last_city
    while current != -1:
        path.append(current)
        prev = parent[mask][current]
        mask ^= (1 << current)  # Убираем текущий город из маски
        current = prev

    path.reverse()          # Путь был собран в обратном порядке
    path.append(start)      # Добавляем возврат в начальный город

    return min_cost, path


if __name__ == "__main__":
    # Пример матрицы расстояний между 4 городами
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Вызываем функцию TSP, начиная с города 0
    min_cost, path = tsp_with_path(dist, 0)

    print("The optimal route:", " -> ".join(map(str, path)))
    print("Total cost:", min_cost)