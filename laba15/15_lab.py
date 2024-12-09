class TreeNode:
    def __init__(self, value):  # Конструктор класса TreeNode.  Инициализирует узел дерева.
        self.value = value  # Значение узла.
        self.left = None  # Левый поддерево (по умолчанию None).
        self.right = None  # Правый поддерево (по умолчанию None).


def construct_tree(expression):  # Функция для построения бинарного дерева из выражения.
    stack = [] #Стек для хранения узлов, которые будут связаны
    index = 0 #Индекс для перебора символов в строке выражения
    nodes = [] #Список для хранения узлов, которые встречаются на текущем уровне

    while index < len(expression):  # Цикл перебора символов выражения.
        if expression[index].isdigit() or expression[index] == '-':  # Проверка на число или знак минуса.
            number = ''

            while index < len(expression) and (expression[index].isdigit() or expression[
                index] == '-'):  # Сбор числа из последовательности цифр и знаков минуса.
                number += expression[index] #Добавляем символ в число
                print(number)
                index += 1
            new_node = TreeNode(number)  # Создание нового узла с числом.

            if stack:  # Проверка, не пуст ли стек.
                parent = stack[-1]  # Получение родительского узла из стека.
                if parent.left is None:  # Проверка, есть ли левый потомок у родителя.
                    parent.left = new_node  # Добавление нового узла как левого потомка.
                elif parent.right is None:  # Проверка, есть ли правый потомок у родителя.
                    parent.right = new_node  # Добавление нового узла как правого потомка.
            nodes.append(new_node)  # Добавление нового узла в список узлов.

        elif expression[index] == '(':  # Обработка открывающей скобки.
            stack += nodes
            index += 1
        elif expression[index] == ')':  # Обработка закрывающей скобки.
            nodes = []
            stack.pop()
            index += 1
        else:  # Игнорирование других символов (запятых и пробелов).
            index += 1
    return stack[0]  # Возвращение корневого узла.


def pre_order_traversal(node):  # Рекурсивная функция прямого обхода дерева.
    if node:  # Проверка, существует ли узел.
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def in_order_traversal(node):  # Рекурсивная функция центрального обхода дерева.
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)


def post_order_traversal(node):  # Рекурсивная функция концевого обхода дерева.
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')


expression = "8 (4 (2 (1, 3), 6 (5,7)), 12 ( 10(9,11)))"
root_node = construct_tree(expression)

print("Прямой: ", end='')
pre_order_traversal(root_node)
print("\n\nЦентарьный: ", end='')
in_order_traversal(root_node)
print("\n\nКонцевой: ", end='')
post_order_traversal(root_node)
