from typing import List

def find_borders(pattern: str) -> List[int]:
    """
    Вычисляет массив граней (prefix function) для алгоритма Кнута-Морриса-Пратта (KMP).

    Граница (border) — это длина наибольшего собственного префикса строки,
    который также является её суффиксом.

    Аргументы:
        pattern (str): Образец (подстрока), для которого вычисляются границы.

    Возвращает:
        List[int]: Массив длин максимальных граней для всех префиксов строки.
    """
    borders = [0] * len(pattern)
    current_index = 0  # Индекс для отслеживания предыдущей границы

    for i in range(1, len(pattern)):
        # Пока не найдем совпадение или не вернемся к началу
        while current_index > 0 and pattern[current_index] != pattern[i]:
            current_index = borders[current_index - 1]

        # Если символы совпадают, увеличиваем длину границы
        if pattern[current_index] == pattern[i]:
            current_index += 1

        # Сохраняем текущую длину границы
        borders[i] = current_index

    return borders


def kmp_algorithm(text: str, pattern: str) -> List[int]:
    """
    Реализует алгоритм Кнута-Морриса-Пратта (KMP) для поиска всех вхождений подстроки в строке.

    Работает за линейное время O(n + m), где n — длина текста, m — длина образца.

    Аргументы:
        text (str): Текст, в котором производится поиск.
        pattern (str): Образец (подстрока), которую ищем.

    Возвращает:
        List[int]: Список индексов, начиная с которых встречается подстрока в тексте.
    """
    if not pattern:
        return [0]  # Обработка пустого шаблона

    borders = find_borders(pattern)
    result = []
    compare_index = 0  # Текущая позиция в pattern

    for i in range(len(text)):
        # Откатываемся, пока не найдем совпадение или не достигнем начала
        while compare_index > 0 and text[i] != pattern[compare_index]:
            compare_index = borders[compare_index - 1]

        # Если символ совпал, продвигаемся по pattern
        if text[i] == pattern[compare_index]:
            compare_index += 1

        # Если дошли до конца pattern — нашли совпадение
        if compare_index == len(pattern):
            start_index = i - compare_index + 1
            result.append(start_index)
            compare_index = borders[-1]  # Продолжаем поиск следующего вхождения

    return result


if __name__ == "__main__":
    print(f"Result of KMP algorithm: {kmp_algorithm('abca', 'abca')}")         # Ожидание: [0]
    print(f"Result of KMP algorithm: {kmp_algorithm('abcababdabaaba', 'abaaba')}")  # Ожидание: [7]
    print(f"Result of KMP algorithm: {kmp_algorithm('abcababdabaabadd', 'abaaba')}") # Ожидание: []