# Custom AdoptionException
class AdoptionException(Exception):
    pass

# Pet class with InvalidPetAgeException
class Pet:
    def __init__(self, name, age, breed):
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Invalid pet age. Age must be a positive integer.")
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} - Age: {self.age}, Breed: {self.breed}"

# PetShelter class with NullReferenceException
class PetShelter:
    def __init__(self):
        self.available_pets = []

    def add_pet(self, pet):
        if pet is None or any(prop is None for prop in [pet.name, pet.age, pet.breed]):
            raise NullPointerException("Pet information is missing.")
        self.available_pets.append(pet)

    def list_available_pets(self):
        for pet in self.available_pets:
            if any(prop is None for prop in [pet.name, pet.age, pet.breed]):
                raise NullPointerException("Pet information is missing.")
            print(pet)

# Donation class with InsufficientFundsException
class Donation:
    def __init__(self, donor_name, amount):
        if not isinstance(amount, (int, float)) or amount < 10:
            raise InsufficientFundsException("Insufficient donation amount. Minimum donation is $10.")
        self.donor_name = donor_name
        self.amount = amount

    def record_donation(self):
        print(f"Donation of ${self.amount} recorded.")

# File handling with FileHandlingException
class PetFileHandler:
    @staticmethod
    def read_pets_from_file(filename):
        try:
            with open(filename, 'r') as file:
                # Assuming each line in the file represents a pet's information
                pet_data = [line.strip().split(',') for line in file.readlines()]
                pets = [Pet(name, int(age), breed) for name, age, breed in pet_data]
                return pets
        except FileNotFoundError:
            raise FileHandlingException(f"File '{filename}' not found.")
        except Exception as e:
            raise FileHandlingException(f"Error reading file '{filename}': {str(e)}")

