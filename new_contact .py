import csv
import os

FILE_NAME = "contacts.csv"

contacts = {}

def save_contacts():
    with open(FILE_NAME , "w" , newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone"])
        
        for name, info in contacts.items():
            writer.writerow([name, info["phone"]])

def load_contacts():
    global contacts
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME , "r") as file:
            reader = csv.reader(file)
            
            next(reader , None)
            
            for row in reader:
                if len(row) >= 2: 
                    name = row[0]
                    phone = row[1]
                    contacts[name] = {"phone": phone}
                    
        print(f" CSV Database loaded! Found {len(contacts)} contacts.")
    else:
        print("  No previous CSV found. Starting fresh. ")
        initialize_default_data()

def initialize_default_data():
    initial_data = [
        ("sundar" , "1234567890")  ,    ("srinivas" , "9876543210")   , ("joseph", "874575441"),
        ("arindu" , "968766444" )  ,    ("krishna"  , "987758978")    , ("deva", "1579856254"),
        ("deepak" , "987989468")   ,    ("shivansh" , "8976421575")   , ("siddarth", "8973218441"),
        ("avinash", "9468034746")  ,    (" ramit "  , "4876745343")   , ("arindam", "984674989"),
        ("yash"   , "6789351145")  ,    (" nirav "  , "498678599")    , ("pandu", "956984357"),
        ("sruthi" , "4868677699")
    ]
    for name, phone in initial_data:
        add_contact (name, phone , save=False)
    save_contacts()

def add_contact (name, phone , save=True):
    clean_name = name.strip() .lower()
    contacts[clean_name] = {"phone": phone}
    print (f"  Success: Contact '{name}' added/updated. ")
    if save:
        save_contacts()

def delete_contact(name):
    clean_name = name.strip().lower()
    if clean_name in contacts:
        del contacts [clean_name]
        save_contacts()
        print(f" Deleted: Contact '{name}' removed.")
    else:
        print(f" Error: Contact '{name}' not found.")

def search_contact(name):
    clean_name = name.strip().lower()
    if clean_name in contacts:
        phone = contacts[clean_name]["phone"]
        print(f"   Found: {name.title()} ->   {phone}")
    else:
        print(f"  Contact  '{name}'  not found.")

def show_all_contacts():
    print("\n---  ----- Contact List (CSV)  ---- ---")
    if not contacts:
        print("No contacts available.")
    else:
        for name in sorted(contacts.keys()):
            print(f"{name.title()}: {contacts[name]   ['phone']}")
    print("----------------------------")

def main():
    load_contacts()
    
    print("\n---  -- --- CONTACT MANAGER SYSTEM (CSV Version)  --- -- ---")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Search Contact   ")
        print("2. Add New Contact  ")
        print("3. Delete Contact   ")
        print("4. View All Contacts   ")
        print("5. Exit ")
        
        choice = input("Enter choice (1-5) : ")

        if choice == '1':
            name = input(" Enter name : ")
            search_contact(name)

        elif choice == '2':
            name = input("Enter new name: ")
            phone = input("Enter phone number: ")
            add_contact(name , phone)

        elif choice == '3':
            name = input("  Enter name to delete:   ")
            delete_contact(name)

        elif choice == '4':
            show_all_contacts()
        elif choice == '5':
            print("   Exiting..📤📤. Data saved in 'contacts.csv'. Open it in Excel!=  ")
            break
        else:
            print("  Invalid choice. Please enter 1-5 ..... ")

if __name__ == "__main__":
    main()