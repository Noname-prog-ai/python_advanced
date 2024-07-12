## Типы связей между таблицами в схеме

![](../img/cinema_schema_diagram.png)

|   Тип связи    | Таблица 1       | Таблица 2 |
|:--------------:|-----------------|-----------|
| один ко многим | movie_direction | director  |
| один ко многим | movie_direction | movie     |
| один к одному  | oscar_awarded   | movie     |
| один ко многим | movie_cast      | movie     |
| один ко многим | movie_cast      | actors    |