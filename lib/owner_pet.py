class Pet:
    # Define a class variable for allowed pet types
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    
    # Define a class variable to hold all instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner  # Associate the pet with an owner if provided
        Pet.all.append(self)  # Add the instance to the class variable list

        # If an owner is provided, add this pet to the owner's pets list
        if owner is not None:
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Initialize an empty list to hold pets
    
    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)
            pet.owner = self  # Set the owner attribute on the pet
        else:
            raise TypeError("Can only add Pet instances.")

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)