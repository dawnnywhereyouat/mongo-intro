"""
    Eg create operations
"""

from bson import ObjectId
from mongo_client import MongoClient

if __name__ == "__main__":
    mongo_client = MongoClient()
    client = mongo_client.client
    db = client.todo_db  # get the todo_db database
    todos_collection = db.todos  # get the todos collection

    def relationship_with_embedded_doc(person_id, address):
        _id = ObjectId(person_id)

        result = todos_collection.update_one(
            {"_id": _id}, {"$addToSet": {"addresses": address}}
        )
        # addToSet will treat the addresses field as a list, and add the new address to it
