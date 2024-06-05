import mysql.connector

# delete data in table 
def delete(host, username, password, database, table_name):
    print("")

    # The connect() constructor creates a connection to MySQL server and returns
    # a MySQLConnection object
    db = mysql.connector.connect(
        host = host,
        user = username,
        password = password,
        database = database
    ) 

    # .cursor method returns a MySQLCurosr() object, or a subclas of it depending on the passed arguments.
    # The returned object is a cursor.
    cursor = db.cursor()
    sql_Delete_query = "Delete from "+ table_name+"where id = %s"
    Id = inptu("Enter lecturer id : ")
    # .execute method executes the given database operation (query or command)
    cursor.execute(sql_Delete_query, (Id,))

    # This method sends a COMMIT statement to the MySQL server,
    # commiting the current transaction.
    # Since by default Conector/Python does not autocommit,
    # it is important to call this method after every transaction
    # that modifies data for tables that use transactional storage engines.

    db.commit()
    print("One row(s) deleted from "+table_name) 