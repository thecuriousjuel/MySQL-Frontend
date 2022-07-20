def does_database_exists(mycursor, database_name):
    query = 'SHOW DATABASES'
    mycursor.execute(query)

    for database in mycursor:
        if database[0] == database_name:
            return True

    return False


def create_database(mycursor, database_name):
    query = f'CREATE DATABASE {database_name}'
    mycursor.execute(query)

    print('Database created')

    