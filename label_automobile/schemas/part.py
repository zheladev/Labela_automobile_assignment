from ..models.part import Part
from marshmallow_sqlalchemy import ModelSchema


class PartSchema(ModelSchema):
    class Meta:
        model = Part