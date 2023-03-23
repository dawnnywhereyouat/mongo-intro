"""
    Eg delete operations
"""

from bson import ObjectId
from mongo_client import MongoClient

if __name__ == "__main__":
    mongo_client = MongoClient()
    client = mongo_client.client
    db = client.todo_db  # get the todo_db database
    todos_collection = db.todos  # get the todos collection

    result = todos_collection.delete_one({"_id": ObjectId("641ab78c44ed5a53ba044b49")})
    print(result.acknowledged)
