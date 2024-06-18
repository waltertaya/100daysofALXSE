from mongoengine import Document, StringField, DateTimeField, IntField

class Owner(Document):
    lease_date = DateTimeField(required=True)
    full_name = StringField(required=True, max_length=255)
    length = IntField()
    user_id = StringField(required=True, unique=True)

    meta = {
        'collection': 'owners'
    }
