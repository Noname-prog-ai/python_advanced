import sqlite3

conn = sqlite3.connect('hw_1_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                    id INTEGER PRIMARY KEY,
                    car_number TEXT,
                    car_name TEXT,
                    description TEXT,
                    owner TEXT
                )''')

cars_data = [
    (1, 'у314ом77', 'chevrolet', 'помятый задний бампер', 'киприянов а. и.'),
    (2, 'о006оо178', 'lorraine-dietrich', 'царапины на левом крыле', 'петриенко м. ю.'),
    (3, 'к994хе78', 'tesla', 'только с завода', 'петриенко м. ю.'),
    (4, 'с569тв78', 'lorraine-dietrich', 'помятая левая дверь, царапина на переднем бампере', 'комаренко и. п.'),
    (5, 'с614са23', 'alfa romeo', 'лобовое стекло в трещинах', 'шарко п. к.'),
    (6, 'с746ор78', 'tesla', 'только с завода, проблема с документами', 'петриенко м. ю.'),
    (7, 'н130ке777', 'lorraine-dietrich', 'раритетная модель, перебрать двигатель', 'силагадзе л. с.'),
    (8, 'н857ск27', 'lada', 'не заводится, без внешних повреждений', 'петриенко м. ю.'),
    (9, 'у657са77', 'lada', 'не читается vin', 'киприянов а. и.'),
    (10, 'е778ве178', 'ford', 'поменять габаритные лампы, резину на зимнюю', 'яковлева е. а.'),
    (11, 'к886ун68', 'lada', 'клиент жаловался на тёмные выхлопы при езде в городе', 'смитенко с. с.'),
    (12, 'н045мо97', 'lada', 'разбита левая фара, помят передний бампер', 'силагадзе л. с.'),
    (13, 'т682ко777', 'alfa romeo', 'поменять резину на зимнюю. царапина на капоте (?)', 'яковлева е. а.'),
    (14, 'о147нм78', 'chevrolet', 'провести то №9', 'шарко п. к.'),
    (15, 'к110та77', 'lada', 'развал-схождение + замена резины', 'смитенко с. с.'),
    (16, 'е717ое78', 'chevrolet', 'помята водительская дверь, заменить габаритки', 'шарко п. к.'),
    (17, 'у261хо57', 'ford', 'заменить резину, проверить свечи', 'петриенко м. ю.'),
    (18, 'м649ом78', 'alfa romeo', 'непонятные шумы при заводе', 'киприянов а. и.'),
    (19, 'с253но90', 'ford', 'заменить аккумулятор, проверить свечи', 'комаренко и. п.'),
    (20, 'а757ах11', 'nissan', 'то, клиент жалуется, что машину косит влево', 'глухих к. и.')
]

cursor.executemany('''INSERT INTO cars (id, car_number, car_name, description, owner)
                      VALUES (?, ?, ?, ?, ?)''', cars_data)

conn.commit()
conn.close()