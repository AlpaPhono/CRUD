import mysql.connector

# insert data into table 
def insert(host, username, password, database, table_name):
    try:
        db = mysql.connector.connect(
            host = host,
            user = username,
            password = password,
            database = database
        )
        # A display to insert data
        id = input("Enter Lecturer ID: ")
        fname = input("Enter Lecturer First Name: ")
        lname = input("Enter Lecturer Last Name: ")
        age = input("Enter Age: ")
        phone_num = input("Enter Phone Number: ")
        department = input("Enter Department: ")

        cursor = db.cursor()
        sql = "insert into " + table_name + "(id, fname, lname, age, phone_num, department) values(%s, %s, %s, %s, %s, %s)"
        print(sql)

        val = (id, fname, lname, age, phone_num, department)
        cursor.execute(sql, val)
        db.commit()

        # For a connection obtained from a connection pool,
        # close() does not actually close it but returns it to the pool
        # ad makes it available for subsequent connection requests.
        db.close()
        print('One record inserted into ' + table_name)
        
    except:
        # .rollback method sends a ROLLBACK statement to the MySQL Server,
        # undoing all data changes from the current transaction
        # by default, Connector/Python does not auto commit,
        # so it is possible to cancel transactions when using transactional storage engines such as InnoDB
        db.rollback()