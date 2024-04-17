"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""
from typing import List

T9_DICT = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def my_t9(input_numbers: str) -> List[str]:
    if not input_numbers:
        return []

    def generate_combinations(current_word, remaining_numbers, results):
        if not remaining_numbers:
            results.append(current_word)
            return

        for letter in T9_DICT[remaining_numbers[0]]:
            generate_combinations(current_word + letter, remaining_numbers[1:], results)

    results = []
    generate_combinations('', input_numbers, results)

    # Представим, что мы пользуемся настоящим словарем, чтобы отфильтровать только правильные английские слова.
    valid_words = [word for word in results if
                   word in ['basement', 'example', 'other']]  # replace with a real dictionary

    return valid_words


if __name__ == '__main__':
    numbers: str = input('>')
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
