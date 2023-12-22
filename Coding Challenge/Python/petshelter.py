from connector import create_connection
from mysql.connector import Error
from pet import Pet
pidc=103
class PetShelter:
    def __init__(self,available_pets):
        self.available_pets=available_pets
    
    

   

    def add_pet_to_database():
        connection = create_connection()
        if connection:
            try:
                name=("enter name:")
                age=input("enter the age=")
                breed = input("Enter breed name: ")
                pid=102

                cursor = connection.cursor()
                cursor.execute("INSERT INTO pets (petid, name, age, breed) VALUES (%s, %s, %s, %s)",
                           (pid,name,age,breed,))
                connection.commit()

                print("Donation recorded successfully!")

            except (Error, ValueError) as e:
                print(f"Error recording donation: {e}")
            finally:
                connection.close()
    add_pet_to_database()