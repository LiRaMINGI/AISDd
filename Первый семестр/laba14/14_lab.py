import hashlib

def sha256_hash_function(word):
    # Хеш-функция SHA-256
    sha256 = hashlib.sha256()
    sha256.update(word.encode('utf-8'))
    # Возвращаем числовое значение хеша
    return int(sha256.hexdigest(), 16)

def create_hash_table(input_file, output_file):
    # Открываем файл с текстом для чтения
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Создаем хеш-таблицу с использованием списка списков
    hash_table_size = len(text.split())  # Размер таблицы равен количеству слов
    hash_table = [[] for _ in range(hash_table_size)] # Создаем список

    # Налагаем хеш на слова из текста и записываем их в хеш-таблицу
    words = text.split()
    for word in words:
        # Используем числовое значение хеша в качестве индекса в таблице
        hash_value = sha256_hash_function(word) % hash_table_size

        # Добавляем слово в список в соответствующий список хеша
        hash_table[hash_value].append(word)

    # Открываем файл для записи результата
    with open(output_file, 'w', encoding='utf-8') as result_file:
        # Записываем хеш-таблицу в файл
        for index, words_list in enumerate(hash_table):
            if words_list:  # Проверяем, что список не пустой
                words = ', '.join(words_list)
                result_file.write(f"{index}: {words}\n")

# Пример использования
create_hash_table('14input.txt', '14output.txt')


