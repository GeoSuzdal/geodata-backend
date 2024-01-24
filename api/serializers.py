import uuid

from rest_framework import serializers
from api.models import Records


class RecordSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    created_at = serializers.DateTimeField()
    record_id = serializers.CharField(max_length=36, default=uuid.uuid4)
    title = serializers.CharField(max_length=120)
    body = serializers.CharField()
    image = serializers.CharField(max_length=48)


class GeojsonSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    created_at = serializers.DateTimeField()
    geojson_obj = serializers.JSONField()
    tag = serializers.CharField(max_length=32)