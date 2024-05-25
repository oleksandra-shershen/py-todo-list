from django.contrib import admin

from app.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
