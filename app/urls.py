from django.conf.urls.static import static
from django.urls import path

from app.views import TaskListView, TagListView, TagCreateView
from to_do_list import settings

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "app"
