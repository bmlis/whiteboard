from marshmallow import fields, Schema


class WorkoutSchema(Schema):
    id = fields.Str(dump_only=True)
    activity_type = fields.Str(required=True)
