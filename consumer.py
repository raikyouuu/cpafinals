import json
from emailsender import send_email, get_owner_email

def search_apartments():
    try:
        with open('apartment_details.json', 'r') as file:
            apartments = json.load(file)
        
        print("\n=== Apartment Search ===")
        search_query = input("Enter the apartment type (e.g., 'studio', '2-bedroom') to search: ").strip().lower()

        matching_apartments = [apt for apt in apartments if search_query in apt['title'].lower()]
        
        if not matching_apartments:
            print(f"No apartments found for '{search_query}'. Please try again with a different query.")
            return

        print(f"\nFound {len(matching_apartments)} {search_query} apartments:\n")
        
        for idx, apartment in enumerate(matching_apartments, start=1):
            print(f"#{idx} - {apartment['title']} | Location: {apartment['location']} | Price: {apartment['price']}")
        
        while True:
            try:
                apartment_number = int(input("\nEnter the apartment number to inquire (0 to exit): ").strip())
                
                if apartment_number == 0:
                    return  
                
                if 1 <= apartment_number <= len(matching_apartments):
                    selected_apartment = matching_apartments[apartment_number - 1]
                    print(f"\nYou selected: #{apartment_number} - {selected_apartment['title']}")
                    print(f"Location: {selected_apartment['location']}")
                    print(f"Price: {selected_apartment['price']}")
                    print(f"Description: {selected_apartment['description']}")
                    
                    owner_email = get_owner_email(selected_apartment)
                    if owner_email:
                        message = input(f"Enter your message for the owner of '{selected_apartment['title']}': ").strip()
                        send_email(owner_email, message)
                    else:
                        print(f"Owner email not found for '{selected_apartment['title']}'")
                    break  
                else:
                    print(f"Invalid number. Please choose a valid apartment number between 1 and {len(matching_apartments)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    except FileNotFoundError:
        print("No apartment details found. Please make sure apartment details are available.")
    except json.JSONDecodeError:
        print("Error reading apartment details file. Please ensure it's formatted correctly.")

if __name__ == "__main__":
    search_apartments()
