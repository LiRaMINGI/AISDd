from typing import List, Dict

def get_bad_characters_dict(pattern: str) -> Dict[str, int]:
    """
    Создаёт словарь последних индексов каждого символа в образце (правило плохого символа).

    Аргументы:
        pattern (str): Образец, по которому строится таблица.

    Возвращает:
        Dict[str, int]: Словарь, где ключ — символ, значение — последняя позиция символа в строке.
    """
    bad_characters_dict = {}

    for i, char in enumerate(pattern):
        bad_characters_dict[char] = i  # Последнее вхождение символа в pattern

    return bad_characters_dict


def bm_algorithm_bad_character(text: str, pattern: str) -> List[int]:
    """
    Реализует часть алгоритма Бойера-Мура — правило плохого символа для поиска подстроки в строке.

    Примечание: Это частичная реализация — только правило плохого символа (без хорошего суффикса).
    Может работать неэффективно или некорректно на некоторых входах без правила хорошего суффикса.

    Аргументы:
        text (str): Текст, в котором производится поиск.
        pattern (str): Подстрока, которую ищем.

    Возвращает:
        List[int]: Список индексов, начиная с которых встречается подстрока в тексте.
    """
    if not pattern or len(pattern) > len(text):
        return []

    symbol_indexes = get_bad_characters_dict(pattern)
    result = []
    shift = 0
    text_len = len(text)
    pattern_len = len(pattern)

    while shift <= text_len - pattern_len:
        current_index = pattern_len - 1  # Начинаем сравнение с конца

        # Пока совпадают символы, двигаемся влево
        while current_index >= 0 and pattern[current_index] == text[shift + current_index]:
            current_index -= 1

        if current_index == -1:  # Полное совпадение найдено
            result.append(shift)

            # Эвристика совпадения
            if shift + pattern_len < text_len:
                next_char = text[shift + pattern_len]
                shift += pattern_len - symbol_indexes.get(next_char, -1)
            else:
                shift += 1

        else:
            # Получаем следующий символ из текста, который вызвал несовпадение
            bad_char = text[shift + current_index]

            # Вычисляем сдвиг по правилу плохого символа
            bad_shift = symbol_indexes.get(bad_char, -1)
            shift += max(1, current_index - bad_shift)

    return result


if __name__ == "__main__":
    print(f"Result of BM algorithm (bad character rule): {bm_algorithm_bad_character('abca', 'abca')}")          # Ожидается: [0]
    print(f"Result of BM algorithm (bad character rule): {bm_algorithm_bad_character('abcababdabaaba', 'abaaba')}")   # Ожидается: [7]
    print(f"Result of BM algorithm (bad character rule): {bm_algorithm_bad_character('abcababdabaabadd', 'abaaba')}") # Ожидается: []