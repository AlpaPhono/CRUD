import mysql.connector

# update data into table 
def update(host, username, password, database, table_name):
    db = mysql.connector.connect(
        host = host,
        user = username,
        password = password,
        database = database
    )
    id = input("Enter Lecturer ID: ")
    fname = input("Enter Lecturer First Name: ")
    lname = input("Enter Lecturer Last Name: ")
    age = input("Enter Age: ")
    phone_num = input("Enter Phone Number: ")
    department = input("Enter Department: ")

    cursor = db.cursor()
    try:
        sqlFormula = "UPDATE "+table_name+" SET fname = %s WHERE id = %s"
        cursor.execute(sqlFormula, (fname, id))

        sqlFormula = "Update "+table_name+"SET lname = %s WHERE id = %s"
        cursor.execute(sqlFormula, (lname, id))

        sqlFormula = "Update "+table_name+"SET age = %s WHERE id = %s"
        cursor.execute(sqlFormula, (age, id))
        
        sqlFormula = "Update "+table_name+"SET phone_num = %s WHERE id = %s"
        cursor.execute(sqlFormula(phone_num, id))

        sqlFormula = "Update "+table_name+"SET department = %s WHERE id = %s"
        cursor.execute(sqlFormula(department, id))

        db.commit()

        print("entries updated in " + table_name)

    except:
        db.rollback()


