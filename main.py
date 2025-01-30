import pyodbc

# Database connection string
connectionString = "Driver={ODBC Driver 17 for SQL Server};UID=sa;PWD=examlyMssql@123;Server=localhost;Database=TestDatabase;Trusted_Connection=No;Persist Security Info=False;Encrypt=No"

# Connect to database
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

# Create Users table (if not exists)
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Users')
    BEGIN
        CREATE TABLE Users (
            ID INT IDENTITY(1,1) PRIMARY KEY,
            Name NVARCHAR(100),
            Email NVARCHAR(100)
        )
    END
""")
conn.commit()
print("Users table is ready.")

# Function to insert a user
def insert_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    cursor.execute("INSERT INTO Users (Name, Email) VALUES (?, ?)", (name, email))
    conn.commit()
    print(f"User '{name}' added successfully.")

# Function to fetch all users
def fetch_users():
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()
    if rows:
        print("\n📌 Users in Database:")
        for row in rows:
            print(f"ID: {row.ID}, Name: {row.Name}, Email: {row.Email}")
    else:
        print("⚠ No users found.")

# Function to update a user
def update_user():
    user_id = input("Enter User ID to update: ")
    name = input("Enter New Name: ")
    email = input("Enter New Email: ")
    cursor.execute("UPDATE Users SET Name = ?, Email = ? WHERE ID = ?", (name, email, user_id))
    conn.commit()
    print(f"User ID {user_id} updated.")

# Function to delete a user
def delete_user():
    user_id = input("Enter User ID to delete: ")
    cursor.execute("DELETE FROM Users WHERE ID = ?", (user_id,))
    conn.commit()
    print(f"User ID {user_id} deleted.")

# Main loop for user interaction
while True:
    print("\n Choose an option:")
    print("1.Insert User")
    print("2.Fetch Users")
    print("3.Update User")
    print("4.Delete User")
    print("5.Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        insert_user()
    elif choice == "2":
        fetch_users()
    elif choice == "3":
        update_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")

# Close connection
cursor.close()
conn.close()
