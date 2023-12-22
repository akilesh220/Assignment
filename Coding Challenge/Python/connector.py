import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            port='3306',
            database="petpals"
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def display_pet_listings():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM pets where availableforadoption=1")
            pets = cursor.fetchall()

            print("Available Pets:")
            for pet in pets:
                print(f"{pet[1]} - Age: {pet[2]}, Breed: {pet[3]}")

        except Error as e:
            print(f"Error retrieving pet listings: {e}")
        finally:
            connection.close()

donation_counter = 1000

def generate_donation_number():
    global donation_counter
    donation_counter += 1
    return donation_counter
# Task 2: Donation Recording           
def record_cash_donation():
    connection = create_connection()
    if connection:
        try:
            donation_number=generate_donation_number()
            donor_name = input("Enter donor name: ")
            amount = float(input("Enter donation amount: "))
            donation_date = datetime.now().strftime("%Y-%m-%d")

            cursor = connection.cursor()
            cursor.execute("INSERT INTO donations (donationid, donarname, donationamount, donationdate) VALUES (%s, %s, %s, %s)",
                           (donation_number,donor_name, amount, donation_date))
            connection.commit()

            print("Donation recorded successfully!")

        except (Error, ValueError) as e:
            print(f"Error recording donation: {e}")
        finally:
            connection.close()

# Task 3: Adoption Event Management
            
participant_counter = 1100

def generate_participant_number():
    global participant_counter
    participant_counter += 1
    return participant_counter

def manage_adoption_event():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM adoptionevents")
            events = cursor.fetchall()

            print("Upcoming Adoption Events:")
            for event in events:
                print(f"Event ID: {event[0]}, Date: {event[1]}, Location: {event[2]}")
            
            participant_no=generate_participant_number()
            event_id = int(input("Enter the Event ID to register: "))
            participant_name = input("Enter your name: ")

            cursor.execute("INSERT INTO participants (participantid, eventid, participantname ) VALUES (%s, %s, %s)",
                           (participant_no, event_id, participant_name))
            connection.commit()

            print("Registration successful!")

        except (Error, ValueError) as e:
            print(f"Error managing adoption event: {e}")
        finally:
            connection.close()



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



#display_pet_listings()
#record_cash_donation()
#manage_adoption_event()
#display_pet_values()