from django.db import models


class Record(models.Model):
    id = models.CharField(max_length=16)
    filename = models.FileField(upload_to=None, max_length=100)
    title = models.CharField(max_length=16)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)


class GeoJSON(models.Model):
    id = models.CharField(max_length=16)
    tag = ""
    obj = ""
