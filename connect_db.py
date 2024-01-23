#!/usr/bin/python3
# connect to MySQLdb

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to dB
    database = MySQLdb.connect(
            host="localhost",
            port=3306, user="root",
            passwd="chr0n!ken",
            db="test_db")

    _cursor = db.cursor()
    # connect to database
    # try:
    #     db = MySQLdb.connect(
    #         host="localhost",
    #         port=3306, user="root",
    #         passwd="chr0n!ken",
    #         db="bank_schema")

    #     _cursor = db.cursor()
        
    #     # run query that might raise an error
    #     _cursor.execute("SELECT * FROM customer")
        
    #     db.commit()
    # # 
    # except MySQLdb.Error as error:
    #     error_code = error.args[0]

    #     if error_code == 1146:
    #         print("table doesn't exist")
    #     elif error_code == 1045:
    #         print("Access denied: invalid user authentication")
    #     else:
    #         print(f"Error {error_code}: {error}")
    
    # finally:
    #     _cursor.close()
    #     db.close()

    # create table
    # _cursor.execute("CREATE TABLE song (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL)")
    
    try:
        _cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(test_db)
        )
    except MySQLdb.Error as err:
        error_code = err.args[0]

        if error_code == 1146:
            print("table does not exist")
        elif error_code == 1045:
            print("access denied: invalid authentication")
        else:
            print(f"Error {error_code}: {err}")
    finally:
        _cursor.close()
        database.close()