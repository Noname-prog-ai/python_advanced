import sqlite3

conn = sqlite3.connect('hw_2_database.db')
cur = conn.cursor()

cur.execute("SELECT colour, COUNT(colour) FROM table_phones GROUP BY colour ORDER BY COUNT(colour) DESC LIMIT 1")
most_frequent_colour = cur.fetchone()[0]
print("Телефоны цвета", most_frequent_colour, "чаще всего покупают.")

cur.execute("SELECT colour, COUNT(colour) FROM table_phones GROUP BY colour")
phone_colours = cur.fetchall()
red_count = next((count for colour, count in phone_colours if colour.lower() == "red"), 0)
blue_count = next((count for colour, count in phone_colours if colour.lower() == "blue"), 0)
if red_count > blue_count:
    print("Красные телефоны покупают чаще синих.")
elif red_count < blue_count:
    print("Синие телефоны покупают чаще красных.")
else:
    print("Красные и синие телефоны покупают примерно одинаково.")

cur.execute("SELECT colour, COUNT(colour) FROM table_phones GROUP BY colour ORDER BY COUNT(colour) ASC LIMIT 1")
least_popular_colour = cur.fetchone()[0]
print("Самый непопулярный цвет телефона -", least_popular_colour)

cur.close()
conn.close()