from django.conf.urls.static import static
from django.urls import path

from to_do_list import settings

from app.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "app"
