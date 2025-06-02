from typing import NewType
import math

# Определяем пользовательский тип Point для представления точки на плоскости
Point = NewType("Point", tuple[float, float])


def polar_angle(p0: Point, p1: Point) -> float:
    """
    Вычисляет полярный угол точки p1 относительно точки p0.
    
    Используется для сортировки точек вокруг начальной точки.
    """
    return math.atan2(p1[1] - p0[1], p1[0] - p0[0])


def cross_product(o: Point, a: Point, b: Point) -> float:
    """
    Вычисляет векторное (косое) произведение (a - o) × (b - o).
    
    Используется для определения направления поворота трех точек:
    - Положительное значение: поворот против часовой стрелки.
    - Отрицательное значение: поворот по часовой стрелке.
    - Ноль: точки коллинеарны.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def graham_scan(points: list[Point]) -> list[Point]:
    """
    Реализует алгоритм Грэхема для построения выпуклой оболочки.

    Алгоритм:
    1. Находит точку с минимальной Y-координатой (и минимальной X, если есть совпадения).
    2. Сортирует все точки по полярному углу относительно этой точки.
    3. Использует стек для построения выпуклой оболочки,
       удаляя точки, образующие невыпуклый угол.

    Возвращает список точек, входящих в выпуклую оболочку (в порядке против часовой стрелки).
    """
    assert len(points) >= 3

    # Шаг 1: Находим самую нижнюю (и самую левую при равенстве) точку
    starting_point = min(points, key=lambda p: (p[1], p[0]))

    # Шаг 2: Сортируем остальные точки по возрастанию полярного угла от starting_point
    sorted_points = sorted(points, key=lambda p: (polar_angle(starting_point, p), p[0], p[1]))

    # Шаг 3: Инициализируем стек первыми двумя точками после starting_point
    stack = [starting_point, sorted_points[0], sorted_points[1]]

    # Шаг 4: Обрабатываем оставшиеся точки
    for point in sorted_points[2:]:
        # Удаляем верхнюю точку из стека, если текущая тройка образует почасовую стрелку
        while len(stack) >= 2 and cross_product(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)

    return stack


if __name__ == "__main__":
    # Блок ввода данных
    N = int(input("Please, enter the number of points: "))
    assert N >= 3
    points = []
    for i in range(N):
        x, y = map(float, input(f"Please, enter the coordinates of {i + 1}th point (x y): ").split())
        points.append((x, y))

    # Вызываем функцию построения выпуклой оболочки
    convex_hull = graham_scan(points)

    # Выводим результат
    if convex_hull:
        print("Convex hull consists of points: ")
        for point in convex_hull:
            print(point)
    else:
        print("Convex hull does not exist for this set of points.")