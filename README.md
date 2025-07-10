# Library-Book-Management-System
 Core Components
BOOK_FILE = 'books.json': Stores book information as { book_id: book_title }.

ISSUE_FILE = 'issued.json': Stores issued books as { student_name: [book_id, issue_date] }.

📌 Functions Overview
✅ load_data(file)
Reads and returns data from the specified JSON file.

If the file doesn't exist, returns an empty dictionary.

✅ save_data(file, data)
Writes data (dictionary) to the given JSON file using json.dump().

📘 add_book()
Takes a Book ID and Title from the user.

Checks for ID duplication.

Saves the book in books.json.

🗑️ remove_book()
Deletes a book by its ID from books.json.

Informs the user if the ID doesn't exist.

📖 issue_book()
Verifies if the book exists.

Records the student's name and the issue date (today's date).

Saves the record in issued.json.

📥 return_book()
Gets student name, looks up issued book.

Calculates the number of days since issue.

Applies a fine of ₹10/day if more than 14 days.

Displays all relevant return info.

Removes the record from issued.json.

🧭 menu()
CLI loop to select operations:

markdown
Copy
Edit
1. Add Book
2. Remove Book
3. Issue Book
4. Return Book
5. Exit
🧠 Example Scenario
Input:
yaml
Copy
Edit
Enter Book ID: B101
Enter Book Title: Python Basics
Issue:
yaml
Copy
Edit
Enter Book ID to issue: B101
Enter Student Name: Riya
Return (after 17 days):
yaml
Copy
Edit
Book ID: B101
Issued on: 2025-06-23
Returned on: 2025-07-10
Total Days: 17
Fine: ₹30
✅ Strengths
Simple and easy to follow.

Uses JSON for persistent storage (human-readable).

Calculates fine correctly.

Clean separation of concerns in functions.

💡 Suggestions for Improvement
1. Prevent Issuing the Same Book Multiple Times
Currently, the system allows the same book to be issued to multiple students.
Solution: Check if a book is already issued before assigning.

python
Copy
Edit
for issued_book in issued.values():
    if issued_book[0] == book_id:
        print("Book already issued to another student.\n")
        return
2. Add Book List and Issued Book List Options
Let users see all books or currently issued books.

3. Allow Multiple Book Issues Per Student
Right now, a student can only have one book. You could change issued[student] to a list of books.

Example structure:

json
Copy
Edit
{
    "Riya": [["B101", "2025-07-01"], ["B102", "2025-07-03"]]
}
4. Improve Fine Calculation Logic
Optional: Give grace days per book category or apply dynamic fine rates.

5. Data Validation
Check that Book ID isn't empty.

Validate date formats, numeric inputs.

Convert names to consistent format (e.g., .strip().title()).

