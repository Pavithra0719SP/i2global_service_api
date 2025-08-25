from api import mongo, bcript
import uuid
from flask_jwt_extended import create_access_token


def register_user(user_email,password,user_name):
    user = mongo.db.users.find_one({'user_email':user_email})
    if user:
        return {'error':'User already exists'},409
    hashed_password = bcript.generate_password_hash(password).decode('utf-8')
    user_id = str(uuid.uuid4())
    new_user = {
        'user_id':user_id,
        'user_name':user_name,
        'user_email':user_email,
        'password':hashed_password,
        "create_on":mongo.db.command('serverStatus')['localTime'],
        "last_update":mongo.db.command('serverStatus')['localTime']
    }
    mongo.db.users.insert_one(new_user)
    return {'message':'User registered successfully'},201

    
def authenticate_user(user_email,password):
    user = mongo.db.users.find_one({'user_email':user_email})
    if not user or not bcript.check_password_hash(user['password'],password):
        return {'error':'Invalid user_email or password'},401
    access_token = create_access_token(identity=user['user_id'])
    return {'access_token':access_token},200