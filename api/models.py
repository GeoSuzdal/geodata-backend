import uuid
from django.db import models


class Records(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    record_id = models.CharField(max_length=36, default=uuid.uuid4)
    title = models.CharField(max_length=120)
    body = models.TextField()
    image = models.CharField(max_length=48)

    class Meta:
        verbose_name = "Record"


class GeojsonObjects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/', default="uploads/default.geojson")
    geojson_obj = models.JSONField()
    tag = models.CharField(max_length=32, unique=True, null=False)

    def __str__(self):
        return f'{self.tag}:{self.file.name}'

    class Meta:
        verbose_name = "GeojsonObject"