from marshmallow2 import Schema, fields


class FooSerializer(Schema):
    _id = fields.Integer()
