from django.conf.urls.static import static

from to_do_list import settings

urlpatterns = [
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


app_name = "app"
