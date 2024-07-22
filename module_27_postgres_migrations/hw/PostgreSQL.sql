Создание базы данных через psql:


psql -U ${POSTGRES_USER} -h localhost
CREATE DATABASE skillbox_db;


Создание таблицы test_psql_table:


\\c skillbox_db
CREATE TABLE test_psql_table (
    id SERIAL PRIMARY KEY,
    example_column VARCHAR(100)
);