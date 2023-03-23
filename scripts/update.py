"""
    Eg update operations
"""

from bson import ObjectId
from mongo_client import MongoClient

if __name__ == "__main__":
    mongo_client = MongoClient()
    client = mongo_client.client
    db = client.todo_db  # get the todo_db database
    todos_collection = db.todos  # get the todos collection

    new_values = {
        "$set": {"status": "done"},  # if field is not exists, it will be created
        "$inc": {"age": 2, "total_sth": 2},  # Increment value
        "$rename": {"status": "is_running", "haha": "HAHA"},  # RENAME FIELD
        "$unset": {  # Remove FIELD
            "hihi": "anything_here_doesnt_matter",
        },
    }
    result = todos_collection.update_one({"tags": "coding"}, new_values)
    print(result.acknowledged)

    def replace_doc(id):
        """
        Replace the entire document without changing the id
        """
        _id = ObjectId(id)

        new_doc = {"new": "foooking", "doc": "mate"}
        result = todos_collection.replace_one({"_id": _id}, new_doc)
