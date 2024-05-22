import datetime

from django.urls import reverse_lazy
from django.views import generic

from app.forms import TagForm
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


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "app/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("app:tag-list")
