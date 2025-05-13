"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
import json
import re
from collections import Counter
from typing import Dict


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    logs = []
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as file:
        for line in file:
            log_data = json.loads(line.strip())
            logs.append(log_data["level"])

    level_counts = Counter(logs)
    return level_counts


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    hours = []
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as file:
        for line in file:
            log_data = json.loads(line.strip())
            log_time = log_data["time"]
            hour = log_time.split(":")[0]
            hours.append(hour)

    hour_counts = Counter(hours)
    most_common_hour = hour_counts.most_common(1)[0][0]
    return int(most_common_hour)


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    critical_logs_count = 0
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as file:
        for line in file:
            log_data = json.loads(line.strip())
            log_time = log_data["time"]
            log_level = log_data["level"]
            if log_time >= "05:00:00" and log_time <= "05:20:00" and log_level == "CRITICAL":
                critical_logs_count += 1

    return critical_logs_count


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    dog_messages_count = 0
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as file:
        for line in file:
            log_data = json.loads(line.strip())
            if "dog" in log_data["message"].lower():
                dog_messages_count += 1

    return dog_messages_count


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    words = []
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as file:
        for line in file:
            log_data = json.loads(line.strip())
            if log_data["level"] == "WARNING":
                message = log_data["message"]
                message_words = re.findall(r'\b\w+\b', message)
                words.extend(message_words)

    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0][0]
    return most_common_word


if __name__ == '__main__':
    tasks = [task1, task2, task3, task4, task5]
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')