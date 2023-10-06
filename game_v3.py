"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 50) -> int:
    """
    Решаем задачу методом половинного деления
    Args:
        number (int, optional): Загаданное число. Defaults to 50.
    Returns:
        int: Число попыток
    """

    count = 1
    predict = 50
    step = predict
    while number != predict:
        count += 1
        step = int(step / 2 + 0.5)
        if number > predict:
            predict += step
        elif number < predict:
            predict -= step

    return count


def score_game(estimated_func) -> int:
    """ За какое количство попыток в среднем
        за 1000 подходов угадывает наш алгоритм

    Args:
        estimated_func ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # фиксируем сид для воспроизводимости
    np.random.seed(777)
    # загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(estimated_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
