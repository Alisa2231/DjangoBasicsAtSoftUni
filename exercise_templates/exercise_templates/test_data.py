import os
import django
from decimal import Decimal
from datetime import date

# Tell Django which settings file to use.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exercise_templates.settings")

# Initialize Django.
django.setup()

# Import models AFTER django.setup()
from books.models import Book
from reviews.models import Review


# ---------------------------------------------------------
# Create books
# ---------------------------------------------------------

books_data = [
    {
        "title": "The Midnight Library",
        "author": "Matt Haig",
        "publisher": "Viking",
        "price": Decimal("18.99"),
        "isbn": "9780525559474",
        "genre": Book.GENRES.FICTION,
        "publishing_date": date(2020, 9, 29),
        "description": (
            "A woman discovers a mysterious library between life and death, "
            "where every book offers a chance to experience a different "
            "version of her life."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9780525559474-L.jpg",
    },
    {
        "title": "Project Hail Mary",
        "author": "Andy Weir",
        "publisher": "Ballantine Books",
        "price": Decimal("21.50"),
        "isbn": "9780593135204",
        "genre": Book.GENRES.SCIENCE,
        "publishing_date": date(2021, 5, 4),
        "description": (
            "A lone astronaut wakes up millions of miles from Earth with "
            "no memory of how he got there and must solve an extraordinary "
            "scientific mystery."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9780593135204-L.jpg",
    },
    {
        "title": "The Name of the Wind",
        "author": "Patrick Rothfuss",
        "publisher": "DAW Books",
        "price": Decimal("17.99"),
        "isbn": "9780756404741",
        "genre": Book.GENRES.FANTASY,
        "publishing_date": date(2007, 3, 27),
        "description": (
            "Kvothe recounts the story of his remarkable life, from his "
            "childhood as a traveling performer to his years studying "
            "magic and music."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9780756404741-L.jpg",
    },
    {
        "title": "Educated",
        "author": "Tara Westover",
        "publisher": "Random House",
        "price": Decimal("16.99"),
        "isbn": "9780399590504",
        "genre": Book.GENRES.BIOGRAPHY,
        "publishing_date": date(2018, 2, 20),
        "description": (
            "A memoir about growing up in a survivalist family and eventually "
            "finding a path to education and a life beyond her isolated upbringing."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9780399590504-L.jpg",
    },
    {
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "publisher": "Celadon Books",
        "price": Decimal("15.99"),
        "isbn": "9781250301697",
        "genre": Book.GENRES.MYSTERY,
        "publishing_date": date(2019, 2, 5),
        "description": (
            "A famous painter stops speaking after being accused of murdering "
            "her husband, while a psychotherapist becomes determined to "
            "uncover the truth."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9781250301697-L.jpg",
    },
    {
        "title": "Sapiens",
        "author": "Yuval Noah Harari",
        "publisher": "Harper",
        "price": Decimal("22.00"),
        "isbn": "9780062316097",
        "genre": Book.GENRES.HISTORY,
        "publishing_date": date(2015, 2, 10),
        "description": (
            "An exploration of human history, examining how Homo sapiens "
            "developed societies, cultures, economies, and systems of belief."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9780062316097-L.jpg",
    },
    {
        "title": "The Martian",
        "author": "Andy Weir",
        "publisher": "Crown Publishing",
        "price": Decimal("19.50"),
        "isbn": "9780804139021",
        "genre": Book.GENRES.SCIENCE,
        "publishing_date": date(2014, 2, 11),
        "description": (
            "An astronaut stranded alone on Mars uses engineering, science, "
            "and determination to stay alive while NASA works to bring him home."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9780804139021-L.jpg",
    },
    {
        "title": "Gone Girl",
        "author": "Gillian Flynn",
        "publisher": "Crown Publishing",
        "price": Decimal("14.99"),
        "isbn": "9780553418361",
        "genre": Book.GENRES.THRILLER,
        "publishing_date": date(2012, 6, 5),
        "description": (
            "When Amy Dunne disappears on her wedding anniversary, suspicion "
            "falls on her husband as the investigation reveals increasingly "
            "disturbing secrets."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9780553418361-L.jpg",
    },
    {
        "title": "The Book Thief",
        "author": "Markus Zusak",
        "publisher": "Knopf",
        "price": Decimal("18.25"),
        "isbn": "9780375842207",
        "genre": Book.GENRES.HISTORY,
        "publishing_date": date(2006, 3, 14),
        "description": (
            "Set in Nazi Germany, a young girl finds comfort in stealing books "
            "and sharing their stories while her family hides a Jewish man."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9780375842207-L.jpg",
    },
    {
        "title": "The Ocean at the End of the Lane",
        "author": "Neil Gaiman",
        "publisher": "William Morrow",
        "price": Decimal("16.75"),
        "isbn": "9780062459367",
        "genre": Book.GENRES.FANTASY,
        "publishing_date": date(2013, 6, 18),
        "description": (
            "An adult man returns to his childhood home and remembers a "
            "strange friendship and supernatural events that changed his life."
        ),
        "image_url": "https://covers.openlibrary.org/isbn/9780062459367-L.jpg",
    },
]


# Dictionary that will let us easily find a book by title.
books = {}

for data in books_data:
    book, created = Book.objects.get_or_create(
        isbn=data["isbn"],
        defaults=data,
    )

    books[book.title] = book

    if created:
        print(f"Created book: {book.title}")
    else:
        print(f"Book already exists: {book.title}")


# ---------------------------------------------------------
# Create reviews
# ---------------------------------------------------------

reviews_data = [
    {
        "title": "A beautifully hopeful story",
        "author": "Emma Carter",
        "body": (
            "I loved the central idea of exploring the lives we might have "
            "lived. The story is emotional without becoming overly sentimental."
        ),
        "rating": Decimal("4.50"),
        "book": books["The Midnight Library"],
    },
    {
        "title": "Excellent science fiction",
        "author": "Daniel Brooks",
        "body": (
            "The scientific problem-solving is fascinating, and the story "
            "moves quickly. The friendship at the heart of the book was "
            "an unexpected bonus."
        ),
        "rating": Decimal("5.00"),
        "book": books["Project Hail Mary"],
    },
    {
        "title": "A rich fantasy world",
        "author": "Sophie Martin",
        "body": (
            "The world-building and music-related elements are wonderful. "
            "Some sections move slowly, but the characters kept me interested."
        ),
        "rating": Decimal("4.25"),
        "book": books["The Name of the Wind"],
    },
    {
        "title": "Powerful and honest memoir",
        "author": "Michael Evans",
        "body": (
            "This was a fascinating account of growing up in an isolated "
            "environment. The author's journey toward education is "
            "particularly memorable."
        ),
        "rating": Decimal("4.75"),
        "book": books["Educated"],
    },
    {
        "title": "Kept me guessing",
        "author": "Laura Bennett",
        "body": (
            "The mystery unfolds slowly and does a good job of making you "
            "question each character. I finished the last few chapters "
            "in one sitting."
        ),
        "rating": Decimal("4.00"),
        "book": books["The Silent Patient"],
    },
    {
        "title": "An ambitious look at humanity",
        "author": "James Wilson",
        "body": (
            "The book connects major events in human history with broader "
            "ideas about society and culture. Some arguments are simplified, "
            "but it makes for an interesting introduction to the subject."
        ),
        "rating": Decimal("4.25"),
        "book": books["Sapiens"],
    },
    {
        "title": "Smart and entertaining",
        "author": "Olivia Reed",
        "body": (
            "The survival problems are explained in a way that makes "
            "technical details easy to follow. The main character's sense "
            "of humor also keeps the story entertaining."
        ),
        "rating": Decimal("4.75"),
        "book": books["The Martian"],
    },
    {
        "title": "A tense psychological thriller",
        "author": "Noah Thompson",
        "body": (
            "The unreliable perspectives make this book difficult to put "
            "down. There are several moments where the story completely "
            "changes direction."
        ),
        "rating": Decimal("4.50"),
        "book": books["Gone Girl"],
    },
    {
        "title": "Beautiful but heartbreaking",
        "author": "Grace Walker",
        "body": (
            "The unusual narration gives the story a distinctive voice. "
            "The relationships between the characters are especially moving."
        ),
        "rating": Decimal("4.75"),
        "book": books["The Book Thief"],
    },
    {
        "title": "Dreamlike and atmospheric",
        "author": "Henry Collins",
        "body": (
            "This feels like a childhood memory mixed with a dark fairy tale. "
            "The atmosphere is fantastic and the book is surprisingly emotional."
        ),
        "rating": Decimal("4.25"),
        "book": books["The Ocean at the End of the Lane"],
    },
]


for data in reviews_data:
    Review.objects.create(**data)

    print(f"Created review: {data['title']}")


print("\nDone! Test data created successfully.")