import json
import os
import re

def valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def apartment():
    print("=== Apartment Listing System ===")
    

    while True:
        email = input("Please enter your email address: ").strip()
        if valid_email(email):
            break
        else:
            print("Invalid email address. Please enter a valid email.")

    print("\nEnter Apartment Details:")
    title = input("Title (Example: 2-Bedroom Apartment for Rent): ").strip()
    location = input("Location (Example: Manila, Taft): ").strip()
    price = input("Price (Example: PHP 5,000/month): ").strip()
    description = input("Description: ").strip()
    contact = input("Contact Number: ").strip()

    details = {
        'email': email,
        'title': title,
        'location': location,
        'price': price,
        'description': description,
        'contact': contact
    }

    if os.path.exists('apartment_details.json'):
        with open('apartment_details.json', 'r') as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(details)

    with open('apartment_details.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("\nApartment details saved successfully!")

if __name__ == "__main__":
    apartment()
