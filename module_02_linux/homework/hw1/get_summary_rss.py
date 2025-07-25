"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""


def get_summary_rss(ps_output_file_path: str) -> str:
    bytes_total = 0
    with open(ps_output_file_path, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            columns = line.split()
            rss = int(columns[5])
            bytes_total += rss

    units = ['Б', 'Кб', 'Мб', 'Гб', 'Тб']
    unit_index = 0
    while bytes_total >= 1024 and unit_index < len(units) - 1:
        bytes_total /= 1024
        unit_index += 1

    return f'{int(bytes_total)} {units[unit_index]}'


if __name__ == "__main":
    path: str = 'output_file.txt'
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
