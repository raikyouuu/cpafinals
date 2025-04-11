import json

def display_details():
    try:
        with open('apartment_details.json', 'r') as file:
            details = json.load(file)

        print("\n=== Apartment Listing Summary ===")
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
        print("===================================")
    except FileNotFoundError:
        print("No apartment details found. Please run apartment.py first to input details.")

if __name__ == "__main__":
    display_details()
