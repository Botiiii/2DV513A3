from mimetypes import common_types
from os import R_OK
from pickletools import TAKEN_FROM_ARGUMENT1
from venv import create
import mysql.connector



cnx = mysql.connector.connect(user="root",
                              password="",
                              host="127.0.0.1",
                              database='cookbook')

print("connection made")
DB_NAME = "cookbook"

cursor = cnx.cursor(prepared=True)

def create_database(cursor, db_name):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        print('Database created')    
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

create_database(cursor, DB_NAME)

def create_table_category(cursor):
    create_category = "CREATE TABLE IF NOT EXISTS `category` (" \
                      "`c_id` SMALLINT NOT NULL AUTO_INCREMENT,"\
                      "`c_name` varchar(100) NOT NULL,"\
                      "PRIMARY KEY (c_id)"\
                      ") ENGINE = InnoDB"

    try: 
        cursor.execute(create_category)
        print("category table created")
    except mysql.connector.Error as err:
        print(err.msg)

create_table_category(cursor)


def create_table_recipe(cursor):
    create_recipe = "CREATE TABLE IF NOT EXISTS `recipe`(" \
                    "`r_id` SMALLINT NOT NULL AUTO_INCREMENT,"\
                    "`r_description` TEXT NOT NULL,"\
                    "`r_name` varchar(100) NOT NULL,"\
                    "`r_ingredients` TEXT NOT NULL,"\
                    "PRIMARY KEY (r_id)"\
                    ") ENGINE = InnoDB"

    try: 
        cursor.execute(create_recipe)
        print("recipe table created")
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        cnx.commit()

create_table_recipe(cursor)
def showAllRecipes():
    show_all_recipes = "SELECT r_name " \
                       "FROM recipe "

    try:
        print(cursor.execute(show_all_recipes))
        print("show all recipes done")
    except mysql.connector.Error as err:
        print (err.msg)

def showAllRecipeInACategory():
        print('selected')


def addRecipe():
    print('selected')

def addCategory():
    val = "(" + input("Enter a new category name: ") + ")"

    insert_into_category = f"""INSERT INTO category (`c_name`)
                           "VALUES (%s)"""

    try:
        cursor.execute(insert_into_category, val)
    except mysql.connector.Error as err:
        print(err.msg) 
    else:
        cnx.commit()



def create_menu():
    print(" ")
    print("1. See all reciptes")
    print("2. See all recipes in a category")
    print("3. Add recipe")
    print("4. Add category")


def main():

    while True:
      create_menu()
      val = input("Enter a digit: ")
      if val == '0': break
      if val == '1': showAllRecipes()
      if val == '2': showAllRecipeInACategory()
      if val == '3': addRecipe()
      if val == '4': addCategory()


     
main()




