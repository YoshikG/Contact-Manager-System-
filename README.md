 
Contact Manager System 
Python 3
 
INTRODUCTION
The Contact Manager System is a lightweight software application designed to store, retrieve, and manage contact information efficiently. In an era where digital communication is paramount, managing a personal or professional directory is a fundamental necessity. This project utilizes Python to create a Command Line Interface (CLI) tool that persists data using a CSV file. It allows users to perform CRUD (Create, Read, Update, Delete) operations on contact details, ensuring data is saved even after the program terminates.
PROBLEM STATEMENT
Traditional paper-based address books are prone to damage and loss, while complex database software can be resource-heavy and difficult to navigate for simple tasks. Users need a lightweight, portable, and fast solution to manage names and phone numbers without requiring internet connectivity or expensive software licenses. This project addresses the need for a simple, persistent digital address book that can be run on any standard computer.

FUNCTIONAL REQUIREMENTS
The system implements the following functionalities:
	Data Persistence: Automatically load existing contacts from contacts.csv on startup and save changes immediately upon modification.
	Add Contact: Allow users to input a name and phone number. The system sanitizes the name (removes spaces, converts to lowercase) for consistent storage.
	Search Contact: Retrieve a phone number by entering the contact's name.
	Delete Contact: Remove a specific contact from the database permanently.
	View All: Display a sorted list of all contacts currently stored in the system.
	Default Initialization: If no database exists, the system automatically creates one with a predefined set of sample contacts.
NON-FUNCTIONAL REQUIREMENTS
	Performance: The system provides near-instantaneous search results using Hash Map (Dictionary) implementation (Time Complexity: O(1)).
	Usability: A clear, menu-driven Command Line Interface that is easy to understand.
	Reliability: Handles file input/output operations safely, preventing data corruption if the file is missing.
	Portability: The application runs on any machine with Python installed and uses standard CSV files compatible with Excel.

SYSTEM ARCHITECTURE
The system follows a modular architecture:
	Presentation Layer: The main() loop handles user input and displays outputs.
	Logic Layer: Functions like add_contact, Contacts, and delete_contact process the data.
	Data Layer: The csv module manages the physical storage of data in contacts.csv.
DESIGN DECISIONS & RATIONALE
	Use of Python Dictionary: A Python dictionary was chosen as the runtime data structure because it offers O(1) average time complexity for lookups, making search operations extremely fast compared to iterating through lists (O(n)).
	Use of CSV for Storage: CSV was selected over SQL databases (like SQLite) for simplicity and portability. CSV files are human-readable and can be opened in Microsoft Excel or Google Sheets without requiring specialized database viewers.
	Data Sanitization: Names are stored in lowercase with whitespace stripped. This decision prevents duplicate entries caused by capitalization errors (e.g., "Sundar" vs "sundar").
IMPLEMENTATION DETAILS
The core logic is implemented in main.py. Below is the source code used for the project:
import csv import os FILE_NAME = "contacts.csv" contacts = {} def save_contacts(): with open(FILE_NAME, "w", newline="") as file: writer = csv.writer(file) writer.writerow(["Name", "Phone"]) for name, info in contacts.items(): writer.writerow([name, info["phone"]]) def load_contacts(): global contacts if os.path.exists(FILE_NAME): with open(FILE_NAME, "r") as file: reader = csv.reader(file) next(reader, None) # Skip header for row in reader: if len(row) >= 2: contacts[row[0]] = {"phone": row[1]} print(f"	 CSV Database loaded! Found {len(contacts)} contacts.") else: print(" No previous CSV found. Starting fresh.") initialize_default_data() def initialize_default_data(): # ... (Default data initialization logic) save_contacts() def add_contact(name, phone, save=True): clean_name = name.strip().lower() contacts[clean_name] = {"phone": phone} if save: save_contacts() # ... (Rest of the CRUD functions: delete, search, show_all) def main(): load_contacts() while True: # ... (Menu loop logic) pass if __name__ == "__main__": main()




SCREENSHOTS / RESULTS
1. Main Menu: Shows the interactive console with 5 options.
2. Search Result: Shows successful retrieval of a phone number.
3.Excel View: Shows the contacts.csv file opened in spreadsheet software.
 

TESTING APPROACH
The system was tested using Black Box Testing techniques:
	Positive Testing: Entering valid names and numbers.
	Result: Data saved successfully.
	Negative Testing: Searching for a non-existent user.
	Result: "Contact not found" error displayed gracefully.
	Boundary Testing: Deleting the last remaining contact.
	Result: System handles empty dictionary correctly without crashing.
	Persistence Testing: Closing the program and reopening it.
	Result: Previously added contacts were successfully loaded from the CSV.

CHALLENGES FACED
	Case Sensitivity: Initially, inputs like "Arindu" and "arindu" were treated as different contacts. This was resolved by converting all inputs to.lower() before storage in the dictionary.
	File Not Found Error: On the very first run, the program crashed because contacts.csv did not exist. This was fixed by adding an os.path.exists() check in the load_contacts function to initialize default data if the file is missing.
LEARNINGS & KEY TAKEAWAYS
	Learned how to manipulate CSV files using Python's csv library.
	Understood the importance of separating data storage (CSV) from runtime data structures (Dictionaries).
	Gained experience in designing a user-friendly CLI loop (while True).
	Learned how to handle basic file system errors and initialize default states.
 FUTURE ENHANCEMENTS
	Input Validation: Implement Regex to ensure phone numbers are exactly 10 digits.
	GUI Implementation: Upgrade the CLI to a Graphical User Interface using Tkinter or PyQt.
	Multiple Fields: Add support for email addresses and home addresses alongside phone numbers.
 REFERENCES
	RG Dromey Text Book
	Python Essential


