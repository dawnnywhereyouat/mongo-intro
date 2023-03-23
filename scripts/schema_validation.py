"""
    Enforce insert data
"""
import datetime

from mongo_client import MongoClient

book_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["title", "authors", "publish_date", "type", "copies_saled"],
        "properties": {
            "title": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "authors": {
                "bsonType": "array",
                "items": {
                    "bsonType": "objectId",
                    "description": "must be a object and is required",
                },
            },
            "publish_date": {
                "bsonType": "date",
                "description": "must be a date and is required",
            },
            "type": {
                "enum": ["Fiction", "Non-fiction"],
                "description": "must be 'Fiction' or 'Non-fiction' and is required",
            },
            "copies_saled": {
                "bsonType": "int",
                "minimum": 0,
                "description": "must be a interger and greater than 0, is required also",
            },
        },
    }
}

author_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["first_name", "last_name", "dob"],
        "properties": {
            "first_name": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "last_name": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "dob": {
                "bsonType": "date",
                "description": "must be a date and is required",
            },
        },
    }
}


if __name__ == "__main__":
    mongo_client = MongoClient()
    client = mongo_client.client
    db = client.todo_db  # get the todo_db database

    try:
        db.create_collection(name="books")
        db.command("collMod", "books", validator=book_validator)
    except Exception as e:
        print(e)

    try:
        db.create_collection(name="authors")
        db.command("collMod", "authors", validator=author_validator)
    except Exception as e:
        print(e)

    books_collection = db.books
    authors_collection = db.authors

    author_lists = [
        {
            "first_name": "Tieu^~",
            "last_name": "Uzi",
            "dob": datetime.datetime(2000, 2, 20),
        },
        {
            "first_name": "Uncle",
            "last_name": "Ye",
            "dob": datetime.datetime(1995, 5, 30),
        },
    ]

    insterted_ids = authors_collection.insert_many(author_lists).inserted_ids
    # insterted_ids = [1, 2]

    books = [
        {
            "title": "I want it that way",
            "authors": [insterted_ids[0]],
            "publish_date": datetime.datetime(2023, 2, 15),
            "type": "Fiction",
            "copies_saled": 100,
        },
        {
            "title": "I got this on remote control",
            "authors": [insterted_ids[1]],
            "publish_date": datetime.datetime(2023, 2, 15),
            "type": "Non-fiction",
            "copies_saled": 10000,
        },
    ]

    insterted_ids = books_collection.insert_many(books).inserted_ids
    print(insterted_ids)
