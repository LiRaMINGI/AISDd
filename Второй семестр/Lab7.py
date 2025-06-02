from typing import List, Tuple

def the_largest_subarray(array: List[float]) -> Tuple[List[float], float]:
    """
    Реализует алгоритм Кадане для нахождения непрерывного подмассива с наибольшей суммой.

    Алгоритм:
    - Проходим по массиву один раз.
    - Поддерживаем текущую сумму подмассива и максимальную найденную сумму.
    - Если текущая сумма становится отрицательной — сбрасываем её и начинаем новый подмассив.

    Особенность:
    - Если все элементы массива отрицательны, возвращается подмассив из одного наибольшего элемента.

    Аргументы:
        array (List[float]): Массив вещественных чисел.

    Возвращает:
        Tuple[List[float], float]: 
            - Непрерывный подмассив с наибольшей суммой.
            - Сумма этого подмассива.
    """
    if not array:
        return ([], float('-inf'))  # Обработка пустого входного массива

    max_sum = float('-inf')
    current_sum = 0
    start_idx = 0
    end_idx = 0

    for index, elem in enumerate(array):
        current_sum += elem

        if current_sum > max_sum:
            max_sum = current_sum
            end_idx = index

        if current_sum < 0:
            current_sum = 0
            start_idx = index + 1

    # Корректировка, если все элементы отрицательны
    if max_sum < 0:
        max_value = max(array)
        max_index = array.index(max_value)
        return ([max_value], max_value)

    return (array[start_idx:end_idx + 1], max_sum)


if __name__ == "__main__":
    print(f"Result: {the_largest_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")  # Ожидается: [4, -1, 2, 1], 6
    print(f"Result: {the_largest_subarray([2, -1, 2, -1, 2])}")                # Ожидается: [2, -1, 2, -1, 2], 4
    print(f"Result: {the_largest_subarray([-2, -1, -2, -1, -2])}")             # Ожидается: [-1], -1
    print(f"Result: {the_largest_subarray([])}")                              # Ожидается: ([], -inf)