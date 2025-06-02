from queue import LifoQueue  # Импортируем класс LifoQueue для использования стека

class Node:
    # Конструктор класса, инициализирующий узел дерева
    def __init__(self, key):
        self.left = None  # Левый дочерний узел, по умолчанию None
        self.right = None  # Правый дочерний узел, по умолчанию None
        self.val = key  # Значение узла

    # Нерекурсивный обход дерева в порядке "корень -> левый потомок -> правый потомок"
    def traverseNonRecursive(self) -> None:
        stack = LifoQueue()  # Создаем стек для хранения узлов
        stack.put(self)  # Помещаем корень дерева в стек

        while not stack.empty():  # Пока стек не пуст
            current = stack.get()  # Извлекаем узел из стека

            while current:  # Пока текущий узел существует
                print(current.val, end=' ')  # Выводим значение текущего узла
                if current.left:  # Если у текущего узла есть левый потомок
                    stack.put(current.left)  # Помещаем его в стек
                current = current.right  # Переходим к правому потомку

# Функция для создания двоичного дерева из строкового представления
def create_tree(string: str) -> Node:
    return create_subtree(string, 0, len(string))  # Вызываем вспомогательную функцию для создания поддеревьев

# Вспомогательная функция для поиска начального индекса правого поддерева в строке
def find_right_subtree(string: str, start: int, end: int):
    bracket_counter = -1  # Счётчик скобок для отслеживания уровня вложенности
    while True:
        if start >= end:  # Если мы достигли конца строки
            return -1  # Возвращаем -1, что означает отсутствие правого поддерева

        # Если встретили запятую, и мы на уровне 0 (нет открытых скобок), это конец левого поддерева
        if string[start] == ',' and bracket_counter == 0:
            return start + 1  # Возвращаем индекс начала правого поддерева

        if string[start] == '(':  # Если встречаем открывающую скобку, увеличиваем уровень вложенности
            bracket_counter += 1
        if string[start] == ')':  # Если встречаем закрывающую скобку, уменьшаем уровень вложенности
            bracket_counter -= 1
        start += 1  # Переходим к следующему символу

# Функция для создания поддерева на основе подстроки строки
def create_subtree(string: str, start: int, end: int) -> Node:
    while string[start] == ' ' or string[start] == '(':  # Игнорируем пробелы и открывающие скобки
        start += 1
    if start >= end:  # Если индекс выходил за пределы строки
        return None

    number = ''  # Строка для хранения числа
    # Собираем число, пока встречаем цифры
    while string[start] in '1234567890':
        number += string[start]
        start += 1
        if start >= end:  # Если конец строки, создаем узел с числом
            return Node(int(number))
    node = Node(int(number))  # Создаем новый узел с числом

    # Находим индекс правого поддерева в строке
    right_subtree_index = find_right_subtree(string, start, end) - 1

    if right_subtree_index == -1:  # Если нет правого поддерева, генерируем ошибку
        raise Exception("Wrong bracket notation string!")

    if right_subtree_index:  # Если правое поддерево существует
        node.left = create_subtree(string, start + 1, right_subtree_index)  # Рекурсивно создаем левое поддерево
        node.right = create_subtree(string, right_subtree_index + 1, end - 1)  # Рекурсивно создаем правое поддерево
    return node  # Возвращаем созданный узел с поддеревьями

# Основная программа
if __name__ == "__main__":  # Проверяем, что это основной модуль
    # Запрашиваем у пользователя ввод строки в формате линейного представления дерева с скобками
    bt = create_tree(input("Please, enter the linear-bracket string: ").strip())
    print('Traverse without recursion: ')
    bt.traverseNonRecursive()  # Нерекурсивный обход дерева

# Пример строки для ввода: 100(99(40,41),98(30,45))
#80(99(40,41),98(30,45))