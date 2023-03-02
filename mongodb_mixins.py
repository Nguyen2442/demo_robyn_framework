from datetime import datetime
from umongo import Document, fields
from mongo import umongo_instance


@umongo_instance.register
class MongoCreateUpdateMixin(Document):
    create_at = fields.DateTimeField(allow_none=True)
    update_at = fields.DateTimeField(allow_none=True)


    class Meta:
        abstract = True

    def pre_insert(self):
        if not self.create_at:
            self.create_at = datetime.utcnow()
        if not self.update_at:
            self.update_at = datetime.utcnow()

    def pre_update(self):
        self.update_at = datetime.utcnow()
        
        