import random

while True:
    choice = input("\t\t\tRoll the Dice? Yes/No: ").lower()
    if choice == 'yes':
        # Ask user how many times they want to roll
        while True:
            try:
                num_rolls = int(input("\t\tHow many times do you want to roll the dice?: "))
                if num_rolls > 0:
                    break
                else:
                    print("Please enter a positive number!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Roll the dice the specified number of times
        print(f"\nRolling dice {num_rolls} time(s):")
        print("-" * 30)
        
        for i in range(num_rolls):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"Roll {i + 1}: ({die1}, {die2})")
        
        print("-" * 30)
        print()  # Empty line for better formatting
        
    elif choice == 'no':
        print("\t\t\t\tThanks For Playing Game!")   
        break
    else:
        print("Invalid Choice!")