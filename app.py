from flask import Flask
from flask import render_template
from database_operations import * 
import mysql.connector
import logging

# Connecting to the database
mydb = mysql.connector.connect(host='localhost', user='root', password='1212')
mycursor = mydb.cursor()

database_name = 'students'
output = does_database_exists(mycursor, database_name)

if not output:
    create_database(mycursor, database_name)
    print('Database')
    


