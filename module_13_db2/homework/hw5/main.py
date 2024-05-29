import sqlite3
import random


def generate_test_data(
        cursor: sqlite3.Cursor,
        number_of_groups: int
) -> None:
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS uefa_commands (id INTEGER PRIMARY KEY, name TEXT, country TEXT, level TEXT)')

    cursor.execute('CREATE TABLE IF NOT EXISTS uefa_draw (command_id INTEGER, group_id INTEGER)')

    strong_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    medium_teams = ['Team F', 'Team G', 'Team H', 'Team I', 'Team J']
    weak_teams = ['Team K', 'Team L', 'Team M', 'Team N', 'Team O']

    all_teams = strong_teams + medium_teams + weak_teams
    random.shuffle(all_teams)

    for i, team in enumerate(all_teams):
        if team in strong_teams:
            level = 'Strong'
        elif team in medium_teams:
            level = 'Medium'
        else:
            level = 'Weak'
        cursor.execute('INSERT INTO uefa_commands (name, country, level) VALUES (?, ?, ?)', (team, 'Country', level))
        cursor.execute('INSERT INTO uefa_draw (command_id, group_id) VALUES (?, ?)',
                       (i + 1, random.randint(1, number_of_groups)))


if __name__ == '__main__':
    number_of_groups: int = int(input('Введите количество групп (от 4 до 16): '))
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        generate_test_data(cursor, number_of_groups)
        conn.commit()
