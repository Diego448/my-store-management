from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient('localhost', 27017)
database = client.my_store_management

users = database.users

def get_users():
    cursor = users.find() 
    return list(cursor)

def get_user(user_id):
    result = users.find_one({"_id": ObjectId(user_id)})
    result['_id'] = user_id
    return result

def add_user(data):
    result = users.insert_one(data)
    return result.acknowledged

def edit_user():
    pass

def delete_user():
    pass