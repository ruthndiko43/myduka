Create a new project called MyDuka with the following files: -main.py -database.py

Open up a new terminal and run the following commands:

pip install flask
pip install psycopg2-binary
TABLES -> Products , Sales , Stock, Users Open sql shell create a new database create database myduka; connect to myduka d. atabase \c myduka

run the following commands

products table CREATE TABLE products ( id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, buying_price NUMERIC(20, 2) NOT NULL CHECK (buying_price >= 0), selling_price NUMERIC(20, 2) NOT NULL CHECK (selling_price >= 0) );

stock table CREATE TABLE stock ( id SERIAL PRIMARY KEY, pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE, stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

sales table CREATE TABLE sales ( id SERIAL PRIMARY KEY, pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE, quantity INTEGER NOT NULL CHECK (quantity > 0), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

users CREATE TABLE users ( id SERIAL PRIMARY KEY, full_name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, phone_number VARCHAR(100) NOT NULL, password VARCHAR(255) NOT NULL );

pip -> pip installs packages

Psycopg2 -> A database driver or adapter used to connect Python to a Postgres database -> To estabish this connection , we use a function called psycopg2.connect() -> which takes some parameters important for establishing a db connection

psycopg2.connect() - a function used to establish a new connection to a postgres db -> It takes some arguments: 1.host - on what server is my database located? - host = 'localhost' localhost : my own device -> database is locally hosted on my device

2.port -> where in my device is the Postgres service running -> Postgres runs on port 5432 by default port = '5432' 3.user - username attached to a Postgres user user = 'postgres' 4.password - password attached to a Postgres user for login password = '1234' 5.dbname - the database you intend to connect to dbname = 'myduka'

127.0.0.1 build an app -> deploy it on cloud to make it available online -> an ip address is assigned to your application

179.181.200.120 domain name -> a human friendly name attached to an ip address https://meet.google.com/dsh-idtb-oqb

cur - an object / tool for performing database operations db operations - select , insert , update , delete

C - create - insert R - read. - select U - update. - update D - delete - delete

cur.execute() - a function used to execute sql queries cur.fetchall() - a function used to retrieve data from Postgres to Python

insert into products(name, buying_price,selling_price)values('bread',50,60); insert into products(name, buying_price,selling_price)values('milk',50,60);

our data format - a list of tuples

Task

insert two record of sales in sql shell and use psycopg2 to display them in your terminal
brush up on the following concepts: -> SQL ( sql queries , joins , aggregate functions , group by) -> Python ( data types, lists and tuples , for loops, if statements & functions) w3schools & geeks for geeks