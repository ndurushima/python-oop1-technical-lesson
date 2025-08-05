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