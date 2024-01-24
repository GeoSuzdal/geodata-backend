from django.contrib import admin
from django.urls import include, path
from api import views


urlpatterns = [
    path("records/", views.records_list, name="records"),
    path("records/<str:record_id>", views.record_by_id, name="record"),
    path("geojson/", views.current_geojson, name="current geojson"),
]