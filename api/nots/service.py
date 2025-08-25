from api import mongo, bcript
import uuid
from flask_jwt_extended import create_access_token

def create_note(note_title, note_content, user_id):
    note_id = str(uuid.uuid4())
    new_note = {
        'note_id': note_id,
        'note_title': note_title,
        'note_content': note_content,
        'user_id': user_id,
        "create_on": mongo.db.command('serverStatus')['localTime'],
        "last_update": mongo.db.command('serverStatus')['localTime']
    }
    mongo.db.notes.insert_one(new_note)
    return {'message': 'Note created successfully', 'note_id': note_id}, 201

def get_notes_by_user(user_id):
    notes = list(mongo.db.notes.find({'user_id': user_id}, {'_id': 0}))
    return {'notes': notes}, 200

def update_note(note_id, note_title, note_content, user_id):
    note = mongo.db.notes.find_one({'note_id': note_id, 'user_id': user_id})
    if not note:
        return {'error': 'Note not found'}, 404
    updated_note = {
        'note_title': note_title,
        'note_content': note_content,
        "last_update": mongo.db.command('serverStatus')['localTime']
    }
    mongo.db.notes.update_one({'note_id': note_id}, {'$set': updated_note})
    return {'message': 'Note updated successfully'}, 200    

def delete_note(note_id, user_id):
    note = mongo.db.notes.find_one({'note_id': note_id, 'user_id': user_id})
    if not note:
        return {'error': 'Note not found'}, 404
    mongo.db.notes.delete_one({'note_id': note_id})
    return {'message': 'Note deleted successfully'}, 200
    
def get_note_by_id(note_id, user_id):    
    note = mongo.db.notes.find_one({'note_id': note_id, 'user_id': user_id}, {'_id': 0})
    if not note:
        return {'error': 'Note not found'}, 404
    return {'note': note}, 200
