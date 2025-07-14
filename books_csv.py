import pandas as pd

# Book data with intentional similarities
data = {
    "title": [
        "Harry Potter and the Sorcerer's Stone",
        "Harry Potter and the Chamber of Secrets",
        "The Hobbit",
        "The Lord of the Rings: Fellowship of the Ring",
        "The Silmarillion",
        "Pride and Prejudice",
        "Sense and Sensibility",
        "Emma",
        "To Kill a Mockingbird",
        "Go Set a Watchman",
        "1984",
        "Animal Farm",
        "Brave New World",
        "Fahrenheit 451",
        "The Catcher in the Rye",
        "Great Expectations",
        "Oliver Twist",
        "Moby Dick",
        "The Old Man and The Sea",
        "The Great Gatsby"
    ],
    "authors": [
        "J.K. Rowling",
        "J.K. Rowling",
        "J.R.R. Tolkien",
        "J.R.R. Tolkien",
        "J.R.R. Tolkien",
        "Jane Austen",
        "Jane Austen",
        "Jane Austen",
        "Harper Lee",
        "Harper Lee",
        "George Orwell",
        "George Orwell",
        "Aldous Huxley",
        "Ray Bradbury",
        "J.D. Salinger",
        "Charles Dickens",
        "Charles Dickens",
        "Herman Melville",
        "Ernest Hemingway",
        "F. Scott Fitzgerald"
    ],
    "description": [
        "A young boy discovers he is a wizard and attends a magical school.",
        "The second year at the magical school with new challenges for the young wizard.",
        "A hobbit embarks on a journey with dwarves to reclaim treasure guarded by a dragon.",
        "The quest to destroy a powerful ring with the fellowship across Middle-earth.",
        "A collection of mythopoeic stories about the history of Middle-earth.",
        "A classic romance that explores manners, marriage, and morality in 19th-century England.",
        "A story of love, romance, and societal expectations in England.",
        "A tale of a young woman navigating love and society in England.",
        "A story of racial injustice and childhood in the Deep South.",
        "The continuation of the story of Scout and her life in the South.",
        "A dystopian society under constant surveillance by a totalitarian regime.",
        "An allegorical novella reflecting events leading up to the Russian Revolution.",
        "A dystopian society where technology controls society and individuality is lost.",
        "A society where books are banned, and firemen burn any that are found.",
        "A young man narrates his experiences in New York after being expelled from school.",
        "The growth and personal development of an orphan named Pip.",
        "The adventures of an orphan in the underworld of London.",
        "A sailor's obsessive quest for revenge on a giant whale.",
        "An aging fisherman struggles with a giant marlin far out in the Gulf Stream.",
        "A mysterious millionaire's passion and obsession in 1920s America."
    ]
}

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)