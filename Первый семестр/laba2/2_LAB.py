def calculate(expression):  # Принимает строку с выражением, пытается вычислить его.
    try:
        return str(evaluate_expression(expression))  # Пытается вычислить выражение и возвращает результат в виде строки.
    except Exception as e:
        return f"Error: {e}"  # Возвращает любые ошибки, возникшие во время вычисления.


def evaluate_expression(expression):  # Организует процесс вычисления.
    tokens = tokenize(expression)  # Разбивает входную строку на токены
    postfix = infix_to_postfix(tokens)  # Преобразует выражение из инфиксной нотации в постфиксную.
    return evaluate_postfix(postfix)  # Вычисляет постфиксное выражение и возвращает результат.

def tokenize(expression):  # Разделяет строку выражения на отдельные токены
    tokens = []
    current_token = ""
    for char in expression: # Цикл перебирает каждый символ в входной строке.
        if char.isdigit() or char == ".": # Проверяет, является ли символ цифрой или точкой.
            current_token += char # Если да, то добавляет символ к текущему токену.
        else: # Если не пустой, то добавляет его в список токенов.
            if current_token:  # Если не пробел, то добавляет символ как отдельный токен.
                tokens.append(current_token)
                current_token = ""
            if char != " ": # Проверяет, не пустой ли текущий токен после цикла
                tokens.append(char)
    if current_token:
        tokens.append(current_token)
    return tokens


def infix_to_postfix(tokens):
    output = []
    stack = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}  # Словарь приоритетов операторов.

    for token in tokens:
        if token.replace(".", "", 1).isdigit():  # Если токен — число
            output.append(token) #Добавляем
        elif token == "(":  # Если токен — открывающая скобка
            stack.append(token) #Помещаем в стек
        elif token == ")":  # Если токен — закрывающая скобка
            while (stack and stack[-1] != "("):
                output.append(stack.pop())  # Извлекаем операторы до открывающей скобки.
            stack.pop()  # Убираем открывающую скобку из стека.
        else:  # Если токен — оператор
            while (stack and stack[-1] != "(" and precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())  # Извлекаем операторы с большим или равным приоритетом.
            stack.append(token)  # Добавляем текущий оператор в стек.

    while stack:
        output.append(stack.pop())  # Добавляем оставшиеся операторы в выходные данные.

    return output


def evaluate_postfix(tokens):
    stack = []
    for token in tokens:
        if token.replace(".", "", 1).isdigit():  # Если токен — число
            stack.append(float(token))  # Преобразуем в число и добавляем в стек.
        else:  # Если токен — оператор
            operand2 = stack.pop()  # Извлекаем два операнда
            operand1 = stack.pop()
            if token == "+":
                stack.append(operand1 + operand2)  # Выполняем операцию
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                stack.append(operand1 / operand2)
    return stack.pop()  # Возвращаем результат



expression = input("Введите выражение: ")
result = calculate(expression)
if result[-4:] == "zero":
    print("Результат равен нулю")
elif result[:5] == "Error":  # Проверяет, была ли ошибка
    print("Некорректное выражение")
else:
    print(f"Результат: {result}")
