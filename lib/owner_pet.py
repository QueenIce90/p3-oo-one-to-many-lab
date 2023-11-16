class Pet:
#- Define a class variable PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]` and validate that the `pet_type` is one of those types in the `__init__` method.
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

#Define a `Pet` and pass into the constructor its `name`, `pet_type` and an optional `owner`.

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

#GETTER / READER
    @property
    def pet_type(self):
        print("GETTING _pet_type")
        return self._pet_type 
  
# SETTER / WRITER
#raise Exception` if this check fails.- Define a class variable `all` that stores all instances of the `Pet` class.
    @pet_type.setter
    def pet_type(self, new_pet_type):
         Hell = Exception
         if new_pet_type not in Pet.PET_TYPES:
             raise Hell(f"{new_pet_type} is not a valid pet type")
         else:
             self._pet_type = new_pet_type
             
    


class Owner:
    def __init__(self, name):
        self.name = name 

# In the `Owner` class write a method called `pets(self)` that returns a full list of the owner's pets.
# to get all your pets / using iteration on the `all` list

    def pets(self):
        return[ pet for pet in Pet.all if pet.owner == self ]
    
# - In the `Owner` class write a method called `add_pet(self, pet)` that checks that the the pet is of type `Pet` and adds the owner to the pet.
# isinstance is used to check if the pet is of type `Pet` and if so add the owner to the pet.
    
    def add_pet(self, new_pet): 
        if isinstance(new_pet, Pet):
            new_pet.owner = self
        else:
            raise Exception("NO")
        
    def get_sorted_pets(self):
        # GET MY PETS 
        my_pets = self.pets()
        # SORT PETS BY NAME
        sorted_pets = sorted( my_pets, key=lambda each_pet: each_pet.name.lower())
    # lambda functions is used to create a lambda function that checks if the pet is of type `Pet` and returns a sorted list of pets by their names.
        # RETURN EM
        return sorted_pets
# -  In the `Owner` class write a method called `get_sorted_pets(self)` returns a sorted list of pets by their names.



# owner can have many pets 
# pet belongs to owner

# Owner --< Pet
 
#Focus

#properties and setters

#making things private with the _ **

# syntac for methods and self 

# isinstance 