from marshmallow import Schema, fields

class UserRigisterSchema(Schema):
    user_name = fields.Str(required=True)
    password = fields.Str(required=True)
    user_email = fields.Email(required=True)
    create_on = fields.DateTime()
    last_update = fields.DateTime()
    user_id = fields.Str() 

class UserLoginSchema(Schema):
     user_email = fields.Email(required=True)
     password = fields.Str(required=True)

     
    
