"""
Mongo Client
"""

import pymongo


class MongoClient:
    """
    Class mongo client
    """

    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb://mongoadmin:password@localhost:27017/"
        )
