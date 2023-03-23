"""
    Advanced queries: regex, ...
"""
import pprint

from mongo_client import MongoClient

if __name__ == "__main__":
    mongo_client = MongoClient()
    client = mongo_client.client
    db = client.todo_db

    # find documents that have at least one character 'I'
    book_containing_a = db.books.find({"title": {"$regex": "I{1}"}})
    # print(list(book_containing_a))

    author_and_books = db.authors.aggregate(
        [
            {
                "$lookup": {
                    "from": "books",  # from "books" collection,
                    "localField": "_id",
                    "foreignField": "authors",
                    "as": "books",
                }
            }
        ]
    )
    # pprint.pprint(list(author_and_books))

    author_books_count = db.authors.aggregate(
        [
            {
                "$lookup": {
                    "from": "books",  # from "books" collection,
                    "localField": "_id",
                    "foreignField": "authors",
                    "as": "books",
                }
            },
            {
                "$addFields": {
                    "total_books": {
                        "$size": "$books",
                    }
                }
            },
            {"$project": {"first_name": 1, "last_name": 1, "total_books": 1, "_id": 0}},
        ]
    )
    # pprint.pprint(list(author_books_count))

    books_with_old_authors = db.books.aggregate(
        [
            {
                "$lookup": {
                    "from": "authors",  # from "books" collection,
                    "localField": "authors",
                    "foreignField": "_id",
                    "as": "authors",
                }
            },
            {
                "$set": {
                    "authors": {  # replace the value in the "authors" field
                        "$map": {  # since "authors" field is a array so we need to map
                            "input": "$authors",
                            "in": {
                                "age": {
                                    "$dateDiff": {
                                        "startDate": "$$this.dob",
                                        "endDate": "$$NOW",
                                        "unit": "year",
                                    }
                                },
                                "first_name": "$$this.first_name",
                                "last_name": "$$this.last_name",
                            },
                        },
                    }
                }
            },
            {
                "$match": {
                    "$and": [
                        {"authors.age": {"$gte": 20}},
                        {"authors.age": {"$lte": 25}},
                    ]
                }
            },
            {"$sort": {"age": 1}},
        ]
    )
    pprint.pprint(list(books_with_old_authors))
