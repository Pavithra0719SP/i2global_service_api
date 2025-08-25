from marshmallow import Schema, fields

class NotsSchema(Schema):
    note_title = fields.Str(required=True)
    note_content = fields.Str(required=True)
    create_on = fields.DateTime()
    last_update = fields.DateTime()
    user_id = fields.Str() 
    note_id = fields.Str()



     
    
