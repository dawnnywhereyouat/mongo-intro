"""
    Eg get operations
"""
import datetime
from bson.objectid import ObjectId

from mongo_client import MongoClient

if __name__ == "__main__":
    mongo_client = MongoClient()
    client = mongo_client.client
    db = client.todo_db  # get the todo_db database
    todos_collection = db.todos  # get the todos collection

    cursor = todos_collection.find()  # this will returns a generator
    for index, doc in enumerate(cursor):
        print(index,doc)
    print(list(cursor))     # since the cursor is a generator, this wont be able to consume the data

    cursor = todos_collection.find_one({"name": "Ye"})  # this will returns a generator
    print(cursor)

    cursor = todos_collection.find({"tags": "coding"})  # this will returns a generator
    for i, data in enumerate(cursor):
        print(i, data)

    cursor = todos_collection.find_one({"_id": "641ab78c44ed5a53ba044b47"})
    print(cursor) # this wont work since id in a document is a ObjectId datatype, not a string
    cursor = todos_collection.find_one({"_id": ObjectId("641ab78c44ed5a53ba044b47")})
    print(cursor) # the right way

    print("Total documents in the collection:", todos_collection.count_documents(filter={}))
    # u cant query instead of using the empty dict {}

    d = datetime.datetime(2023, 3, 23)
    cursor = todos_collection.find({"due_date": {"$lt": d}}).sort("status")
    print(list(cursor)) # the right way

    def get_age_range(min_age, max_age):
        query = {
            "$and": [
                {"age": {"$gte": min_age}},
                {"age": {"$lte": max_age}},
            ]
        }
        cursor = todos_collection.find(query).sort("age")


    def get_specific_columns():
        cols = {"_id": 0, "name": 1}
        # except the '_id' field, which field is not in the dict wont be returned
        cursor = todos_collection.find({}, cols)
        print(list(cursor))