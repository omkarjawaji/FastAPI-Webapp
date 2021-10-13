from mongoengine import Document, StringField, IntField, ListField, BooleanField

class Startups(Document):
    id = IntField()
    name = StringField(max_length=50)
    type = StringField()
    is_listed = BooleanField()
    