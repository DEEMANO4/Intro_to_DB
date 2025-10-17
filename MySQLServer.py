import mysql.connector

DB_Host = 3306,
DB_User = "root",
DB_Password = "Uwomanodavidapena_1",
DataBase_Name = "alx_book_store"

try:
    mydb = mysql.connector.connect(
        host = DB_Host,
        user = DB_User,
        password = DB_Password,
        database = DataBase_Name
    
    )

    mycursor = mydb.cursor()
    create_db_query = f"CREATE DATABASE IF NOT EXISTS alx_book_store"
    mycursor.execute()

    print("Database alx_book_store created successfully!")


except mysql.connector.Error as err:
    print(f"Error creating MySQL database: {err}")

finally:
    if mydb in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
