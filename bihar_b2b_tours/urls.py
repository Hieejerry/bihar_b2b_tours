from django.contrib import admin
from django.urls import path

from enquiries.views import gallery_manifest, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("gallery-manifest/", gallery_manifest, name="gallery_manifest"),
    path("", home, name="home"),
]
