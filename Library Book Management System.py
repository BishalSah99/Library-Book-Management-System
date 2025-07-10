import datetime
import os
import json

# File names for storing data
BOOK_FILE = 'books.json'
ISSUE_FILE = 'issued.json'

# Load books from file
def load_data(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            return json.load(f)
    return {}

# Save data to file
def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)

# Add a new book
def add_book():
    books = load_data(BOOK_FILE)
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Book ID already exists!")
        return
    book_title = input("Enter Book Title: ")
    books[book_id] = book_title
    save_data(BOOK_FILE, books)
    print("Book added successfully!\n")

# Remove a book
def remove_book():
    books = load_data(BOOK_FILE)
    book_id = input("Enter Book ID to remove: ")
    if book_id in books:
        del books[book_id]
        save_data(BOOK_FILE, books)
        print("Book removed successfully!\n")
    else:
        print("Book ID not found!\n")

# Issue a book to student
def issue_book():
    books = load_data(BOOK_FILE)
    issued = load_data(ISSUE_FILE)
    
    book_id = input("Enter Book ID to issue: ")
    if book_id not in books:
        print("Book ID not found!\n")
        return
    
    student = input("Enter Student Name: ")
    issue_date = datetime.date.today().isoformat()
    
    issued[student] = [book_id, issue_date]
    save_data(ISSUE_FILE, issued)
    print(f"Book issued to {student} on {issue_date}\n")

# Return a book
def return_book():
    issued = load_data(ISSUE_FILE)
    student = input("Enter Student Name: ")
    
    if student not in issued:
        print("No book issued to this student.\n")
        return
    
    book_id, issue_date = issued[student]
    issue_date = datetime.date.fromisoformat(issue_date)
    return_date = datetime.date.today()
    
    days = (return_date - issue_date).days
    fine = 0
    if days > 14:
        fine = (days - 14) * 10  # ₹10 per day after 14 days

    print(f"Book ID: {book_id}")
    print(f"Issued on: {issue_date}")
    print(f"Returned on: {return_date}")
    print(f"Total Days: {days}")
    print(f"Fine: ₹{fine}\n")
    
    del issued[student]
    save_data(ISSUE_FILE, issued)

# Menu
def menu():
    while True:
        print("Library Book Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!\n")

if __name__ == "__main__":
    menu()
