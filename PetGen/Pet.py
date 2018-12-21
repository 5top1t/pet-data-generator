class Pet:
    def __init__(self, id, image, name, breed, age, last_visit, owner):
        self.id = id
        self.image = image
        self.name = name
        self.breed = breed
        self.age = age
        self.last_visit = last_visit
        self.owner = owner

    def __str__(self):
        pet_to_string = "" + str(self.id) + ", "
        pet_to_string += self.image + ", " + self.name + ", "
        pet_to_string += self.breed + ", " + str(self.age) + ", "
        pet_to_string += self.last_visit + ", " + self.owner
        return pet_to_string


def main():
    print("")


if __name__ == "__main__":
    main()