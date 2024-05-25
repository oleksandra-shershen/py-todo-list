import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic, View

from app.forms import TagForm, TaskForm
from app.models import Tag, Task

import matplotlib.pyplot as plt
from io import BytesIO
import base64


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "app/index.html"
    queryset = Task.objects.prefetch_related("tags")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        context["today_datetime"] = datetime.datetime.now()

        return context


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:index")


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


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")


class ToggleTaskStatus(View):
    def post(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return redirect(reverse_lazy("app:index"))


plt.switch_backend("Agg")


def tasks_by_tag_view(request):
    tags = Tag.objects.all()
    tasks_count_by_tag = {tag.name: tag.tasks.count() for tag in tags}

    plt.figure(figsize=(6, 4))
    plt.bar(
        tasks_count_by_tag.keys(),
        tasks_count_by_tag.values(),
        color="skyblue"
    )
    plt.xlabel("Tags")
    plt.ylabel("Number of Tasks")

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    bar_chart_png = buffer.getvalue()
    buffer.close()

    bar_chart = base64.b64encode(bar_chart_png).decode("utf-8")

    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(is_done=True).count()
    pending_tasks = total_tasks - completed_tasks

    plt.figure(figsize=(6, 4))
    labels = ["Completed", "Pending"]
    sizes = [completed_tasks, pending_tasks]
    colors = ["skyblue", "#FF7043"]
    explode = (0.1, 0)
    plt.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=140,
    )

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    pie_chart_png = buffer.getvalue()
    buffer.close()

    pie_chart = base64.b64encode(pie_chart_png).decode("utf-8")

    return render(
        request,
        "app/statistics.html",
        {
            "bar_chart": bar_chart,
            "pie_chart": pie_chart
        }
    )
