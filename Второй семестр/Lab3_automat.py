from typing import List, Dict, Optional

def build_transition_table(pattern: str) -> list[dict[str, int]]:
    """
    Строит таблицу переходов для конечного автомата поиска подстроки.

    Алгоритм:
    - Для каждого состояния (0..m) определяется переход для каждого символа алфавита.
    - Если текущий символ совпадает с символом в паттерне — увеличиваем состояние.
    - Иначе — используем "откат" через уже построенную часть таблицы (похоже на KMP).

    Аргументы:
        pattern (str): Искомая подстрока.

    Возвращает:
        List[Dict[str, int]]: Таблица переходов размером (m+1) x |алфавит|
    """
    m = len(pattern)
    alphabet = {'a', 'b', 'c'}  # Ограничимся этим набором символов
    transition_table = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for c in alphabet:
            # Попробуем продвинуться дальше по паттерну
            next_state = min(m, state + 1)
            # Пока не найдём совпадение или не вернёмся к состоянию 0
            while next_state > 0 and (next_state - 1 >= len(pattern) or pattern[next_state - 1] != c):
                next_state = transition_table[next_state - 1].get(c, 0)
            transition_table[state][c] = next_state

    return transition_table


def finite_automata(text: str, pattern: str) -> Optional[int]:
    """
    Реализует алгоритм поиска подстроки с помощью конечного автомата.

    Аргументы:
        text (str): Текст, в котором ищем.
        pattern (str): Подстрока, которую ищем.

    Возвращает:
        Optional[int]: Индекс первого вхождения подстроки в строку, или None, если не найдено.
    """
    if not pattern:
        return 0  # Пустая подстрока всегда найдена

    transition_table = build_transition_table(pattern)
    n = len(text)
    m = len(pattern)
    state = 0  # Начальное состояние

    for i in range(n):
        current_char = text[i]
        state = transition_table[state].get(current_char, 0)

        if state == m:  # Полное совпадение паттерна
            return i - m + 1  # Возвращаем начальный индекс совпадения

    return None  # Совпадений не найдено


if __name__ == "__main__":
    print(f"Result of finite automaton: {finite_automata('abca', 'abca')}")          # Должно быть: 0
    print(f"Result of finite automaton: {finite_automata('abcababdabaaba', 'abaaba')}")  # Должно быть: 7
    print(f"Result of finite automaton: {finite_automata('abcababdabaabadd', 'abaaba')}") # Не должно находить — вернёт None