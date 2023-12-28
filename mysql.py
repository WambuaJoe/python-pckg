#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_passwd):
    connection = True
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_passwd
        )
        print("Connection to mySQL DB successful")
    except Error as e:
        print(f"Error [{e}] occurred")
    return connection

connection = create_connection('localhost', 'root', '')