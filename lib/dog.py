class Dog:
    def __init__(self, name, breed, age, last_checkup = None):
        self.name = name
        self.breed = breed
        self.age = age
        self.last_checkup = last_checkup
    
    def checkup(self, date):
        print(f"Checking up with {self.name} on {date}.")
        self.last_checkup = date
    
    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age}")

fido = Dog("Fido", "Golden Retriever", 3, "05/22/2022")

clifford = Dog(
    name = "Clifford",
    breed = "Big Red",
    age = 2
)

print(fido.age)
fido.birthday_celebration()
print(fido.age)

print(clifford.last_checkup)
clifford.checkup("03/02/2024")
print(clifford.last_checkup)