from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
database = client.my_store_management
users = database.users

def get_users():
    cursor = users.find() 
    return list(cursor)