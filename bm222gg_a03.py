from os import R_OK
from venv import create
import mysql.connector



cnx = mysql.connector.connect(user="root",
                              password="",
                              host="127.0.0.1",
                              database='localWebShop')

print("connection made")

cursor = cnx.cursor(prepared=True)
DB_NAME = "localWebShop"

def create_database(cursor, db_name):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        print('Database created')    
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

create_database(cursor, DB_NAME)

def create_table_item(cursor):
    create_item = "CREATE TABLE IF NOT EXISTS `item` (" \
                    "`i_id` SMALLINT NOT NULL AUTO_INCREMENT,"\
                    "`i_description` TEXT NOT NULL,"\
                    "`i_name` varchar(100) NOT NULL,"\
                    "`i_link` varchar(500) NOT NULL,"\
                    "`i_ingredientOf` TEXT NOT NULL,"\
                    "PRIMARY KEY (i_id)"\
                    ") ENGINE = InnoDB"

    try: 
        cursor.execute(create_item)
        print("item table created")
    except mysql.connector.Error as err:
        print(err.msg)

create_table_item(cursor)


def create_table_recipe(cursor):
    create_recipe = "CREATE TABLE IF NOT EXISTS `recipe`(" \
                    "`r_id` SMALLINT NOT NULL AUTO_INCREMENT,"\
                    "`r_description` TEXT NOT NULL,"\
                    "`r_title` varchar(100) NOT NULL,"\
                    "`r_time` SMALLINT NOT NULL,"\
                    "PRIMARY KEY (r_id)"\
                    ") ENGINE = InnoDB"

    try: 
        cursor.execute(create_recipe)
        print("recipe table created")
    except mysql.connector.Error as err:
        print(err.msg)

create_table_recipe(cursor)


