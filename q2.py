from multiprocessing import connection import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', database='employee', password='')

if connection.is_connected(): print("Connected to the database.")

print("\n")

use_query = """USE Employee;"""
select_query = """SELECT * FROM employee;""" cursor = connection.cursor() cursor.execute(use_query) cursor.execute(select_query)

print("After select query:") rows1 = cursor.fetchall() for x in rows1:
print(x)

print("\n")

insert_query = """INSERT INTO employee VALUES(6, 'Marketer', 'Mumbai','CMO' ,'50000' );"""
cursor.execute(use_query) cursor.execute(insert_query) cursor.execute(select_query)

print("After insert query:") rows2 = cursor.fetchall()
