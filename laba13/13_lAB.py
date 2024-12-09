import hashlib

def sha256_hash_function(word):
    # Хеш-функция SHA-256
    sha256 = hashlib.sha256() #Создает объект хеш-функции SHA-256
    sha256.update(word.encode('utf-8')) #Обновляем хеш-объект, передав строку, преобразованную в байты
    # Возвращаем числовое значение хеша
    return int(sha256.hexdigest(), 16)

def create_hash_table(input_file, output_file):
    # Открываем файл с текстом для чтения
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Создаем хеш-таблицу с использованием метода наложения
    hash_table_size = len(text.split())  # Размер таблицы равен количеству слов
    hash_table = [None] * hash_table_size #Создаем ячейки(выделяем место)

    # Налагаем хеш на слова из текста и записываем их в хеш-таблицу
    words = text.split()
    for word in words:
        # Используем числовое значение хеша в качестве индекса в таблице
        hash_value = sha256_hash_function(word) % hash_table_size

        # Ищем свободное место, если текущее место занято
        while hash_table[hash_value] is not None:
            hash_value = (hash_value + 1) % hash_table_size

        # Записываем слово в таблицу
        hash_table[hash_value] = word

    # Открываем файл для записи результата
    with open(output_file, 'w', encoding='utf-8') as result_file:
        # Записываем хеш-таблицу в файл
        for index, word in enumerate(hash_table):
            if word is not None:
                result_file.write(f"{index}: {word}\n")

# Пример использования
create_hash_table('13input.txt', '13output.txt')
