import mysql.connector

try:
    mydb = mysql.connector.connect(
    host = 3306,
    user = "root",
    password = "Uwomanodavidapena_1",
    database = "alx_book_store"
    )

    mycursor = mydb.cursor()
    mycursor.execute()

    print("Database alx_book_store created successfully!")


except mysql.connector.Error as err:
    print(f"Error creating MySQL database: {err}")

finally:
    if mydb in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
