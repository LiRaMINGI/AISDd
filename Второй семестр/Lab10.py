from typing import List

def egg_drop(eggs: int, floors: int) -> int:
    """
    Решает задачу о минимальном количестве бросков яиц (egg drop problem).

    Цель: найти минимальное число попыток (бросков), необходимых для определения 
    критического этажа F, при котором яйцо разбивается, используя заданное количество яиц.

    Аргументы:
        eggs (int): Количество доступных яиц.
        floors (int): Общее количество этажей.

    Возвращает:
        int: Минимальное количество бросков, необходимое для нахождения критического этажа.
    """
    # dp[k][m] — максимальное число этажей, которые можно проверить с k яйцами за m бросков
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]

    # Если только одно яйцо — нужно проверять каждый этаж по порядку
    for m in range(1, floors + 1):
        dp[1][m] = m

    # Динамическое программирование для заполнения таблицы
    for k in range(2, eggs + 1):
        for m in range(1, floors + 1):
            dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1

    # Найдём минимальное число бросков, при котором можно покрыть все этажи
    min_throws = -1
    for m in range(1, floors + 1):
        if dp[eggs][m] >= floors:
            min_throws = m
            break

    # Опционально: вывод стратегии бросков
    if min_throws != -1:
        print("Strategy of drops:")
        remaining_throws = min_throws
        current_floor = 0
        step = dp[eggs - 1][remaining_throws - 1] + 1

        while remaining_throws > 0:
            current_floor += step
            remaining_throws -= 1
            if current_floor >= floors:
                print(f"Drop from floor: {floors}")
                break
            print(f"Drop from floor: {current_floor}")
            step = dp[eggs - 1][remaining_throws - 1] + 1

    return min_throws


if __name__ == "__main__":
    print("Minimum number of throws:", egg_drop(2, 100))  # Ожидается: 14