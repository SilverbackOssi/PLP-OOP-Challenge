from pet import Pet  # Assuming your Pet class is in a file called pet.py

def main():
    print("🐾 Welcome to the Virtual Pet Simulator! 🐾")
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Train your pet")
        print("5. Show your pet's tricks")
        print("6. Check your pet's status")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice == 1:
            my_pet.eat()
        elif choice == 2:
            my_pet.sleep()
        elif choice == 3:
            my_pet.play()
        elif choice == 4:
            trick = input("What trick would you like to teach your pet? ")
            my_pet.train(trick)
        elif choice == 5:
            my_pet.show_tricks()
        elif choice == 6:
            my_pet.get_status()
        elif choice == 7:
            print(f"Goodbye! {my_pet.name} will miss you! 🐾")
            break
        else:
            print("Please choose a valid option between 1 and 7.")

if __name__ == "__main__":
    main()
