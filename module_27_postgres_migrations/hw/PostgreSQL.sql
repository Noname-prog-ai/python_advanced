CREATE DATABASE skillbox_db;
GRANT ALL PRIVILEGES ON DATABASE skillbox_db TO <username>;

\c skillbox_db;
CREATE TABLE test_psql_table (id SERIAL PRIMARY KEY, name VARCHAR(50));