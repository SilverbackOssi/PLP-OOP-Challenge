class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 10
        self.happiness = 10
        self.tricks = []  # List to store learned tricks
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating...")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")
    
    def play(self):
        if self.energy > 0:
            self.energy = max(0, self.energy - 2)
            self.hunger = min(10, self.hunger + 1)
            self.happiness = min(10, self.happiness + 2)
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play. Let them rest!")
    
    def get_status(self):
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")
    
    def train(self, trick):
        if self.energy > 1:
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to train. They need rest!")
    
    def show_tricks(self):
        print(f"{self.name}'s learned tricks: {', '.join(self.tricks) if self.tricks else 'None'}")

# My example usage
my_pet = Pet("Max")
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("roll over")
my_pet.train("play dead")
my_pet.get_status()
