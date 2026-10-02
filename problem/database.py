import sqlite3

# Database connect
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    price INTEGER,
    category TEXT
)
""")

# 20 Books
books = [
    (1, "Python Basics", "John Smith", 450, "Programming"),
    (2, "Learn Java", "James Gosling", 550, "Programming"),
    (3, "C Programming", "Dennis Ritchie", 400, "Programming"),
    (4, "Data Structures", "Mark Allen", 600, "Computer Science"),
    (5, "Database Management", "Raghu Ramakrishnan", 700, "Database"),
    (6, "Operating System", "Abraham Silberschatz", 800, "Computer Science"),
    (7, "Computer Networks", "Andrew Tanenbaum", 750, "Networking"),
    (8, "Web Development", "Robert Smith", 500, "Web"),
    (9, "HTML and CSS", "Jon Duckett", 650, "Web"),
    (10, "JavaScript Guide", "David Flanagan", 700, "Web"),
    (11, "Django for Beginners", "William Vincent", 600, "Python"),
    (12, "Artificial Intelligence", "Stuart Russell", 900, "AI"),
    (13, "Machine Learning", "Tom Mitchell", 850, "AI"),
    (14, "Deep Learning", "Ian Goodfellow", 950, "AI"),
    (15, "Clean Code", "Robert Martin", 750, "Programming"),
    (16, "Algorithms", "Thomas Cormen", 1000, "Computer Science"),
    (17, "The Alchemist", "Paulo Coelho", 350, "Novel"),
    (18, "Atomic Habits", "James Clear", 500, "Self Help"),
    (19, "Rich Dad Poor Dad", "Robert Kiyosaki", 450, "Finance"),
    (20, "Think and Grow Rich", "Napoleon Hill", 400, "Self Help")
]


cursor.execute("SELECT * FROM books where category ='AI' ")

data = cursor.fetchall()
for data in data:
    print(data)
