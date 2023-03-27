"""
    Full-text search
"""
import pprint

from mongo_client import MongoClient

if __name__ == "__main__":
    mongo_client = MongoClient()
    client = mongo_client.client
    db = client.todo_db

    def fuzzy_matching():
        result = db.books.aggregate(
            [
                {
                    "$search": {  # $search operation is only available for Mongo Atlas
                        "index": "title_text",  # search index's name that created on Mongo Atlas
                        "text": {
                            "query": "Computer",
                            "path": "title",
                            "fuzzy": {},
                        },  # fuzzy search will allow to search almost complete texts, remove fuzzy to perform exact search
                    }
                }
            ]
        )
        return result

    pprint.pprint(fuzzy_matching())
