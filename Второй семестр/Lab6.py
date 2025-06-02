from typing import List

def rk_algorithm(text: str, pattern: str) -> List[int]:
    """
    Реализует алгоритм поиска подстроки в строке методом Рабина-Карпа.

    Метод использует полиномиальный хэширование для эффективного сравнения подстрок.
    Это позволяет свести временную сложность к O(n + m) в среднем случае,
    где n — длина текста, m — длина образца.

    Аргументы:
        text (str): Текст, в котором производится поиск.
        pattern (str): Подстрока (образец), которую ищем.

    Возвращает:
        List[int]: Список индексов, начиная с которых встречается подстрока в тексте.
    """
    result = []
    base = 256       # Основание для полиномиального хэша
    mod = 101        # Простое число для уменьшения размера хэша
    m = len(pattern)
    n = len(text)

    if m == 0 or m > n:
        return result

    # Предвычисляем значения степени для хэширования
    h_pow = 1
    for _ in range(m - 1):
        h_pow = (h_pow * base) % mod

    # Вычисляем хэш для pattern и первой подстроки text
    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod

    # Скользим окном по тексту
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            # Хэши совпали, проверяем точное совпадение
            if all(pattern[j] == text[i + j] for j in range(m)):
                result.append(i)

        # Обновляем хэш для следующей подстроки
        if i < n - m:
            window_hash = (
                base * (window_hash - ord(text[i]) * h_pow) + ord(text[i + m])
            ) % mod
            window_hash = (window_hash + mod) % mod  # Избегаем отрицательных значений

    return result


if __name__ == "__main__":
    print(f"Result of RK algorithm: {rk_algorithm('abca', 'abca')}")          # Ожидается: [0]
    print(f"Result of RK algorithm: {rk_algorithm('abcababdabaaba', 'abaaba')}")   # Ожидается: [7]
    print(f"Result of RK algorithm: {rk_algorithm('abcababdabaabadd', 'abaaba')}") # Ожидается: []
    print(f"Result of RK algorithm: {rk_algorithm('abcababdabaab', 'ab')}")       # Ожидается: [0, 3, 7]