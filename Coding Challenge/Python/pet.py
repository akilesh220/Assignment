from connector import create_connection
from mysql.connector import Error
class Pet:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    
    def display_pet_values():
        try:
            # Database connection
            connection = create_connection()
            if connection:
                try:
                    cursor = connection.cursor()

                    # Retrieve pet values from the database
                    cursor.execute("SELECT * FROM pets")
                    pets = cursor.fetchall()

                    # Display pet values
                    print("Pet Values in the Database:")
                    for pet in pets:
                        print(f"ID: {pet[0]}, Name: {pet[1]}, Age: {pet[2]}, Breed: {pet[3]}")

                except Error as e:
                    print(f"Error retrieving pet values from the database: {e}")

                finally:
                    connection.close()

        except Error as e:
            print(f"Error connecting to the database: {e}")
    #display_pet_values()