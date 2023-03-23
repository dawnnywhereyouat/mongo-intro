"""Tets
"""
import datetime

import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb://mongoadmin:password@localhost:27017/")
# print(client.list_database_names())

# db = client["customersdb"]
db = client.todo_db  # get the todo_db database
# print(db.list_collection_names()) # list of the collection names
todos = db.todos  # get the todos collection

todo1 = {
    "name": "Hai Dang",
    "task": "Just do it",
    "status": True,
    "tags": ["python", "coding"],
    "due_date": datetime.datetime.now(),
}
# result = todos.insert_one(todo1)
# print(result.inserted_id)   # id of the document
# print(result.acknowledged)  # true / false

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
# result = todos.insert_many(todo_lists)
# print(result.inserted_ids)   # [ObjectId('641ab78c44ed5a53ba044b48'), ObjectId('641ab78c44ed5a53ba044b49')]
# print(result.acknowledged)


cursor = todos.find()  # this will returns a generator
# for index, doc in enumerate(cursor):
#     print(index,doc)
# print(list(cursor))     # since the cursor is a generator, this wont be able to consume the data

cursor = todos.find_one({"name": "Ye"})  # this will returns a generator
# print(cursor)

cursor = todos.find({"tags": "coding"})  # this will returns a generator
# for i, data in enumerate(cursor):
#     print(i, data)


cursor = todos.find_one({"_id": "641ab78c44ed5a53ba044b47"})
# print(cursor) # this wont work since id in a document is a ObjectId datatype, not a string
cursor = todos.find_one({"_id": ObjectId("641ab78c44ed5a53ba044b47")})
# print(cursor) # the right way


print("Total documents in the collection:", todos.count_documents(filter={}))
# u cant query instead of using the empty dict {}

d = datetime.datetime(2023, 3, 23)
cursor = todos.find({"due_date": {"$lt": d}}).sort("status")
# print(list(cursor)) # the right way

# result = todos.delete_one({"_id": ObjectId("641ab78c44ed5a53ba044b49")})
# print(result.acknowledged)

new_values = {
    "$set": {"status": "done"},  # if field is not exists, it will be created
    "$inc": {"age": 2, "total_sth": 2},  # Increment value
    "$rename": {"status": "is_running", "haha": "HAHA"},  # RENAME FIELD
    "$unset": {  # Remove FIELD
        "hihi": "anything_here_doesnt_matter",
    },
}
result = todos.update_one({"tags": "coding"}, new_values)
print(result.acknowledged)


def get_age_range(min_age, max_age):
    query = {
        "$and": [
            {"age": {"$gte": min_age}},
            {"age": {"$lte": max_age}},
        ]
    }
    cursor = todos.find(query).sort("age")


def get_specific_columns():
    cols = {"_id": 0, "name": 1}
    # except the '_id' field, which field is not in the dict wont be returned
    cursor = todos.find({}, cols)
    print(list(cursor))


def replace_doc(id):
    """
    Replace the entire document without changing the id
    """
    _id = ObjectId(id)

    new_doc = {"new": "foooking", "doc": "mate"}
    result = todos.replace_one({"_id": _id}, new_doc)


def relationship_with_embedded_doc(person_id, address):
    _id = ObjectId(person_id)

    result = todos.update_one({"_id": _id}, {"$addToSet": {"addresses": address}})
    # addToSet will treat the addresses field as a list, and add the new address to it
