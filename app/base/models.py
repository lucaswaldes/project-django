from django.db import models
import uuid


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class SoftDelete(BaseModel):
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract=True