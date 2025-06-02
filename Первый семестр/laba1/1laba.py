def f(string):
    M = []
    S = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in S.values():  # Если символ — открывающая скобка
            M.append(char)
        elif char in S.keys():  # Если символ — закрывающая скобка
            if M == [] or M[-1] != S[char]:  # Проверка на несоответствие
                return False
            M.pop()

    return M == []  # Если стек пустой — все скобки закрыты

# Основная часть программы
input_string = input("Введите строку, состоящую из скобок: ")

if not input_string:
    print("Строка не существует")
else:
    if f(input_string):
        print("Строка существует и является правильной")
    else:
        print("Строка существует, но является неправильной")
