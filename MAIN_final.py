import sys
import consumer
import apartment
import os

def show_menu():
    print("\n                    ---- Main Menu ----")
    print("                          1. Renter")
    print("                          2. Owner")
    print("                          3. Exit")

def main():
    while True:
        show_menu()
        choice = input("\n                    Choose an option:")
        os.system('cls')    
        if choice == '1':
            consumer.main()
            os.system('cls')
        elif choice == '2':
            apartment.main()
            os.system('cls')
        elif choice == '3':
            sys.exit()
        else:
            print("Invalid input. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()


    
