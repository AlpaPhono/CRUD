import mysql.connector

# display data
def  display_table_information(host, username, password, database, table_name):

    db = mysql.connector.connect(
        host = host,
        user = username,
        password = password,
        database = database
    )

    # courser method returns a MYSQLCursor() object, or a subclass of it depending on the passed arguments.
    # The returned object is a cursor.
    cursor = db.cursor()

    # Reports whether the connection to MYSQL Server is available.
    if db.is_connected():

        # .execute method executes the given database operation (query or command)
        cursor.execute("SELECT * From"+table_name)

        # row is just a variable 
        # this variable will print every column for each row of data.
        for row in cursor:
            print("\nLecturer ID : ", row[0])
            print("\nFirst Name : ", row[1])
            print("\nLast Name : ", row[2])
            print("\nAge : ", row[3])
            print("\nPhone Number : ", row[4])
            print("\nDepartment : ", row[5])