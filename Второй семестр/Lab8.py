from typing import List, Literal

def coin_exchange(coins: List[int], amount: int) -> float | Literal[-1]:
    """
    Вычисляет минимальное количество монет, необходимое для набора заданной суммы.

    Используется метод динамического программирования.
    
    Аргументы:
        coins (List[int]): Список номиналов доступных монет (предполагается, что каждая > 0).
        amount (int): Целевая сумма, которую нужно набрать.

    Возвращает:
        float | Literal[-1]: Минимальное количество монет для получения суммы `amount`.
                             Если сумму набрать невозможно — возвращает -1.
    """
    # dp[i] — минимальное количество монет, чтобы получить сумму i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суммы 0 нужно 0 монет

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                # Обновляем dp[current_amount], если можно улучшить текущее значение
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    print(coin_exchange([1, 3, 4], 6))         # Ожидается: 2 (3 + 3)
    print(coin_exchange([1], 10))              # Ожидается: 10 (монет по 1)
    print(coin_exchange([1, 2, 5], 100))       # Ожидается: 20 (20 монет по 5)
    print(coin_exchange([3, 5], 7))            # Ожидается: -1 (нельзя набрать 7)
    print(coin_exchange([1, 5, 10, 25], 30))   # Ожидается: 2 (25 + 5)