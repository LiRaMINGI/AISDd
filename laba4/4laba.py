#Сортировка методом прочесывания O(n^2) средний и худший случай;
#O(nlogn)-в лучшем
def sort(arr):
    n = len(arr)
    step = n
    factor = 1.3  # Коэффициент уменьшения шага
    sorted = False

    while not sorted:
        # Уменьшаем шаг для следующего прохода
        step = max(1, int(step / factor))
        #print(step)
        sorted = step == 1  # Предполагаем, что массив отсортирован при step = 1

        print(arr)
        # Проходим по массиву с текущим шагом
        for i in range(n - step):
            if arr[i] > arr[i + step]:
                print(step, arr[i],arr[i+step])
                # Если элементы не в порядке, меняем их
                arr[i], arr[i + step] = arr[i + step], arr[i]
                sorted = False  # Устанавливаем флаг, что сортировка не завершена

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("Исходная последовательность:", arr)

    # Сортируем
sort(arr)

print("Отсортированная последовательность:", arr)