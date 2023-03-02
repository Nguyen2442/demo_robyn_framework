from mongo import umongo_instance
from umongo import fields
from mongodb_mixins import MongoCreateUpdateMixin


@umongo_instance.register
class Fruit(MongoCreateUpdateMixin):
    name = fields.StringField(default=False, allow_none=True)

    class Meta:
        collection_name = "Fruit"