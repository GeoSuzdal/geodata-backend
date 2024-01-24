from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api import serializers
from api.models import Records, GeojsonObjects


@api_view(["GET"])
def records_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        records = Records.objects.all()
        serializer = serializers.RecordSerializer(data=records, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.validated_data)


@api_view(["GET"])
def record_by_id(request, record_id):
    if request.method == "GET":
        record = Records.objects.get(record_id=record_id)
        serializer = serializers.RecordSerializer(data=record.__dict__, many=False)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


@api_view(["GET"])
def current_geojson(request):
    if request.method == "GET":
        obj = GeojsonObjects.objects.get(tag="main")
        serializer = serializers.GeojsonSerializer(data=obj.__dict__, many=False)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)