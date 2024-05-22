import datetime
from django.views import generic

from app.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "app/index.html"
    queryset = Task.objects.prefetch_related("tags")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        context["today_datetime"] = datetime.datetime.now()

        return context
