from typing import Dict, List, Optional, Literal

def can_color(graph: Dict[int, List[int]], k: int) -> Optional[Dict[int, int]]:
    """
    Проверяет, можно ли раскрасить граф с использованием не более чем `k` цветов,
    так чтобы соседние вершины имели разные цвета (используется backtracking).

    Аргументы:
        graph (Dict[int, List[int]]): Граф в виде словаря смежности.
        k (int): Количество доступных цветов.

    Возвращает:
        Optional[Dict[int, int]]: Раскраска в виде словаря {вершина: цвет}, или None, если невозможно.
    """
    # Сортируем вершины по убыванию степени (жадная эвристика для ускорения)
    nodes = sorted(graph.keys(), key=lambda node: -len(graph[node]))
    colors = {}  # Текущая раскраска

    def backtrack(node_index: int) -> Optional[Dict[int, int]]:
        """
        Рекурсивная функция, которая пытается раскрасить вершины по порядку.
        """
        if node_index == len(nodes):
            return colors.copy()  # Все вершины раскрашены

        current_node = nodes[node_index]
        for color in range(1, k + 1):
            # Проверяем, используется ли этот цвет среди соседей
            if all(colors.get(neighbor) != color for neighbor in graph[current_node]):
                colors[current_node] = color  # Пробуем цвет
                result = backtrack(node_index + 1)
                if result is not None:
                    return result
                del colors[current_node]  # Откатываем выбор

        return None  # Нет подходящего цвета

    return backtrack(0)


def find_min_colors(graph: Dict[int, List[int]]) -> tuple[int, Dict[int, int]]:
    """
    Находит минимальное количество цветов, необходимое для раскраски графа.

    Алгоритм:
    - Попробует последовательно увеличивать число цветов от 1 до max_degree + 1.
    - Использует `can_color()` для проверки возможности раскраски.

    Аргументы:
        graph (Dict[int, List[int]]): Граф в виде словаря смежности.

    Возвращает:
        tuple[int, Dict[int, int]]: Минимальное число цветов и соответствующая раскраска.
    """
    max_degree = max(len(neighbors) for neighbors in graph.values())  # Максимальная степень вершины
    for k in range(1, max_degree + 2):  # Проверим до max_degree + 1
        coloring = can_color(graph, k)
        if coloring is not None:
            return k, coloring
    # Запасной вариант: столько же цветов, сколько вершин
    return len(graph), {node: i + 1 for i, node in enumerate(graph)}


if __name__ == "__main__":
    # Примеры графов
    graphS = [
        {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2]
        },
        {
            0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [1, 2]
        },
        {
            0: [1, 4, 5],
            1: [0, 2, 3, 7],
            2: [1, 3, 7],
            3: [1, 2, 4, 6],
            4: [0, 3, 5, 6],
            5: [0, 4, 6],
            6: [3, 4, 5, 7],
            7: [1, 2, 6]
        }
    ]

    for idx, graph in enumerate(graphS, start=1):
        k, coloring = find_min_colors(graph)
        print(f"Граф #{idx}:")
        print(f"Минимальное количество цветов: {k}")
        print(f"Раскраска вершин: {coloring}")
        print("-" * 40)

    # Цвет 1 — красный  
    # Цвет 2 — зелёный  
    # Цвет 3 — синий  