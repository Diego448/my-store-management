import re
from fastapi import FastAPI, Request
import db_utils

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Not Implemented!'}

@app.get('/login')
async def login():
    return {'login_status': 'success'}

@app.get('/users')
async def get_users():
    return db_utils.get_users()

@app.post('/user/create')
async def create_user(request: Request):
    data_body = await request.json()
    return db_utils.add_user(data_body)

@app.get('/user/{user_id}')
async def get_user(user_id: str):
    return db_utils.get_user(user_id)