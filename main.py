# import mysql.connector with specified submodule to be used: connect,
# Error and cursor 
from mysql.connector import connect, Error, cursor

# import our own module moduleDB and specified submodule insertData,
# updateData, deleteData and displayData
# The "as" keyword is used to create an alias
from moduleDB import insertData as insert, updateData as update, deleteData as delete, displayData as display

# function 1: create new database
def create_db(username, password):
    try: # try block lets you test a block of code for errors*
        with connect(
            # "host" is server name / targeted server to be connected 
            host = glbHost,
            user = username,
            password = password
        ) as connection:
            dbname = input("What is DB name you want to create? ")
            create_db_query = "CREATE DATABASE "+dbname
            print(create_db_query)
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
            print("Database "+dbname+" is created!")
        # except block lets you handle the error
        pass
    except Error as e:
        print("Ops, something is wrong", e)
    # NameError raised when a variable is not found in local or global scope
    except NameError:
        print("NameError is raised when the identifier being accessed is not defined in the local or global scope.")


# function 2: Delete database
def drop_db(username, password):
    try:
        # database connection
        # set all database credential (host, user, password)
        with connect(
            host = glbHost,
            user = username,
            password = password
        )as connection:
            dbname =input("What is DB name you want to drop?: ")
            drop_db_query = "DROP DATABASE %s" % dbname
            with connection.cursor() as cursor:
                    cursor.execute(drop_db_query)
            print('Database ', dbname, 'has been dropped.')
        pass
    except Error as e:
        print(format(e))



# function3: create table 
def create_table(username, password):
    dbName = input('Enter database name first: ')
    try:
        # database connection
        # set all database credential (host, user, password, database)
        with connect(
            host = glbHost,
            user = username,
            password = password,
            database = dbName
        ) as connection:
            table_name = input ("insert table name you want to create: ")
            create_table_query = "CREATE TABLE "+table_name+"(id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(50), lname VARCHAR(50), age INT, phone_num VARCHAR(50), department VARCHAR(100))"
            print(create_table_query)
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)

            for x in cursor:
                print(x)
    
    except Error as e:
        print(format(e))


# function 4: Delete table
def drop_table(username, password):
    dbName = input(' From which database you want to delete the table?: ')
    try:
        
        # database connection
        # set all database credential (host, user, password)
        with connect(
            host = glbHost,
            user = username,
            password = password
        )as connection:
            dbtable = input(" Enter table name : ")
            drop_table_query = "DROP Tables " + dbtable
            print(drop_table_query)
            with connection.cursor() as cursor:
                cursor.execute(drop_table_query)
                print("Table", dbtable, "has been dropped.")
    except Error as e:
        print(format(e))

# function 5: display all database existed
def show_database(username, password):
    try:
        # database connection
        # set all database credential (host, user, password)
        with connect (
            host = glbHost,
            user = username,
            password = password
        ) as connection:
            cursor = connection.cursor()
            databases = ("show databases")
            cursor.execute(databases)
            i = 0
            for (databases) in cursor:
                i = i + 1
                print("Databases ", i , "is :", databases[0])
    except Error as e:
        print("Ops, something is wrong", e)
    except NameError:
        print("NameError is raised when the identifier being accessed is not defined in the local or global scope.")



#======================================================================
#                       Main code
#======================================================================

# display text 
print("************** POLYTECHNIC MERSING DATABASE***************")
print("1 CREATE DATABASE \n2. DROP DATABASE \n3. CREATE TABLE "
      "\n4. DROP TABLE \n5. INSERT \n6. UPDATE \n7. DELETE "
      "\n8. DISPLAY \n9. SHOW DATABASE \n10. EXIT\n")

while True:
    choice = int(input("Enter your choice :"))
    if choice in range(1,11):

        # glbHost is a global variable for "localhost"
        # "localhost" is the targeted server to be connected
        glbHost = "localhost"
        u = input("Enter Mysql Username: ")
        p = input("Enter Mysql Password: ")
        i = 0
        
        if choice == 1:
            # go create_db function
            create_db(u,p)
        
        elif choice == 2:
            # go to drop_db function
            drop_db(u,p)
        elif choice == 3:
            # got to create_table function
            create_table(u,p)

        elif choice == 4:
            # go to drop_table function
            drop_table(u,p)

        elif choice == 5:
            database = input("Enter database name: ")
            table_name = input("Enter table name: ")
            # go to moduleDB insertData.py
            insert.insert(glbHost, u, p, database, table_name)

        elif choice == 6:
            database = input("Enter database name: ")
            table_name = input("Enter table name: ")
            # go to moduleDB updateData.py
            update.update(glbHost, u, p, database, table_name)

        elif choice == 7:
            database = input("Enter database name: ")
            table_name = input("Enter table name: ")
            # go to moduleDB deleteData.py
            delete.delete(glbHost, u, p, database, table_name)
        
        elif choice == 8:
            database = input("Enter database name: ")
            table_name = input("Enter table name: ")
            # go to moduleDB displayTable.py
            display.display_table_information(glbHost, u, p, database, table_name)
        
        elif choice == 9:
            # go to show database function
            show_database(u,p)
        
        elif choice == 10:
            exit()
        else:
            print("Invalid Input ")