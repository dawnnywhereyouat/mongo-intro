"""
    Eg create operations
"""
import datetime

from mongo_client import MongoClient

if __name__ == "__main__":
    mongo_client = MongoClient()
    client = mongo_client.client
    db = client.todo_db  # get the todo_db database
    todos_collection = db.todos  # get the todos collection

    todo1 = {
        "name": "Hai Dang",
        "task": "Just do it",
        "status": True,
        "tags": ["python", "coding"],
        "due_date": datetime.datetime.now(),
    }
    result = todos_collection.insert_one(todo1)
    print(result.inserted_id)  # id of the document
    print(result.acknowledged)

    todo_lists = [
        {
            "name": "Tieu^~ Uzi",
            "task": "That way",
            "status": False,
            "tags": ["java", "coding"],
            "due_date": datetime.datetime.now(),
        },
        {
            "name": "Ye",
            "task": "I dont care",
            "status": True,
            "tags": ["god", "coding"],
            "due_date": datetime.datetime.now(),
        },
    ]
    result = todos_collection.insert_many(todo_lists)
    print(
        result.inserted_ids
    )  # [ObjectId('641ab78c44ed5a53ba044b48'), ObjectId('641ab78c44ed5a53ba044b49')]
    print(result.acknowledged)
