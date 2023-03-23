"""
Mongo Client
"""

import datetime

import pymongo
from bson.objectid import ObjectId


class MongoClient:
    """
    Class mongo client
    """

    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb://mongoadmin:password@localhost:27017/"
        )
