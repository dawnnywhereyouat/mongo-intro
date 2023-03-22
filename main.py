import datetime
import pymongo 
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb://mongoadmin:password@localhost:27017/")
# print(client.list_database_names())

# db = client["customersdb"]
db = client.todo_db # get the todo_db database
# print(db.list_collection_names()) # list of the collection names
todos = db.todos    # get the todos collection 

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


cursor = todos.find()     # this will returns a generator
# for index, doc in enumerate(cursor):
#     print(index,doc)
# print(list(cursor))     # since the cursor is a generator, this wont be able to consume the data

cursor = todos.find_one({"name": "Ye"})     # this will returns a generator
# print(cursor)

cursor = todos.find({"tags": "coding"})     # this will returns a generator
# for i, data in enumerate(cursor):
#     print(i, data)


cursor = todos.find_one({"_id": "641ab78c44ed5a53ba044b47"})     
# print(cursor) # this wont work since id in a document is a ObjectId datatype, not a string
cursor = todos.find_one({"_id": ObjectId("641ab78c44ed5a53ba044b47")})     
# print(cursor) # the right way


print('Total documents in the collection:', todos.count_documents(filter={}))
# u cant query instead of using the empty dict {}

d = datetime.datetime(2023, 3, 23)
cursor = todos.find({"due_date": {"$lt": d}}).sort("status")     
# print(list(cursor)) # the right way

# result = todos.delete_one({"_id": ObjectId("641ab78c44ed5a53ba044b49")})
# print(result.acknowledged)

result = todos.update_one({"tags": "coding"}, {"$set": {"status": "done"}})
print(result.acknowledged)

