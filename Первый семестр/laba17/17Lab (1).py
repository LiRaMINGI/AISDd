class Node: # Класс представляет узел бинарного дерева
    def __init__(self, data):
        self.data = data # Хранит данные узла
        self.left = None # Левый узел
        self.right = None # Правый узел

# Добавление нового узла
def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

# Функция удаления
def delete(root, key):
    if not root:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

# Ищем минимальное значение в дереве, двигаясь по левым потомкам до низа
def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current

# Поиск пути к числу
def search(root, key, path=None):
    if path is None:
        path = [] # Путь от корня до искомого числа

    # Проверка, является ли текущий узел тем, кого мы ищем
    if not root or root.data == key:
        if root:
            path.append(root.data)
        return root, path

    path.append(root.data)

    # Сначала ищем в левой части, если не нашли ищем в правой
    if key < root.data:
        return search(root.left, key, path)
    return search(root.right, key, path)

# Алгоритм обхода дерева
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Меню опереций
def print_menu():
    print("\nВыберите операцию:")
    print("1. Добавить вершину")
    print("2. Удалить вершину")
    print("3. Найти вершину")
    print("4. Вывести дерево")
    print("5. Выйти из программы")

# Вывод дерева
def print_tree(root):
    print("\nДерево (в виде линейно-скобочной записи):")
    print_tree_format(root)

# Вывод конструкции дерева
def print_tree_format(root):
    if not root:
        return
    print(root.data, end=" ")
    if root.left or root.right:
        print("(", end=" ")
        print_tree_format(root.left)
        print(", ", end=" ")
        print_tree_format(root.right)
        print(")", end=" ")

#  Само дерево
def main():
    tree = Node(8)
    tree.left = Node(3)
    tree.left.left = Node(1)
    tree.left.right = Node(6)
    tree.left.right.left = Node(4)
    tree.left.right.right = Node(7)
    tree.right = Node(10)
    tree.right.right = Node(14)
    tree.right.right.left = Node(13)

    while True:
        print_menu()
        choice = input("Введите номер операции: ")

        if choice == '1':
            value = int(input("Введите значение для добавления: "))
            tree = insert(tree, value)
            print("Вершина добавлена.")
        elif choice == '2':
            value = int(input("Введите значение для удаления: "))
            tree = delete(tree, value)
            print("Вершина удалена.")
        elif choice == '3':
            value = int(input("Введите значение для поиска: "))
            result, path = search(tree, value)
            if result:
                print(f"Вершина {value} найдена. Путь к вершине: {path}")
            else:
                print(f"Вершина {value} не найдена.")
        elif choice == '4':
            print_tree(tree)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()

