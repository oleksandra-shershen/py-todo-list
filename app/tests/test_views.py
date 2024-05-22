from django.test import TestCase
from django.urls import reverse
from app.models import Task, Tag
from datetime import date


class TaskListViewTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name="urgent")
        self.task1 = Task.objects.create(
            title="Task 1", deadline=date(2024, 6, 1), is_done=False
        )
        self.task1.tags.add(self.tag1)

    def test_task_list_view(self):
        response = self.client.get(reverse("app:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/index.html")
        self.assertIn("task_list", response.context)
        self.assertIn("today_datetime", response.context)
        self.assertEqual(len(response.context["task_list"]), 1)
        self.assertEqual(response.context["task_list"][0].title, "Task 1")


class TaskCreateViewTest(TestCase):

    def test_task_create_view(self):
        response = self.client.post(
            reverse("app:task-create"),
            {"title": "New Task", "deadline": "2024-06-01", "is_done": False},
        )
        self.assertEqual(
            response.status_code, 302
        )  # Redirection after successful creation
        self.assertRedirects(response, reverse("app:index"))
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, "New Task")


class TaskUpdateViewTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title="Task 1", deadline=date(2024, 6, 1), is_done=False
        )

    def test_task_update_view(self):
        response = self.client.post(
            reverse("app:task-update", args=[self.task.pk]),
            {
                "title": "Updated Task",
                "deadline": "2024-06-01",
                "is_done": False
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("app:index"))
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task")


class TaskDeleteViewTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title="Task 1", deadline=date(2024, 6, 1), is_done=False
        )

    def test_task_delete_view(self):
        response = self.client.post(reverse(
            "app:task-delete",
            args=[self.task.pk]
        )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("app:index"))
        self.assertEqual(Task.objects.count(), 0)


class TagListViewTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name="urgent")

    def test_tag_list_view(self):
        response = self.client.get(reverse("app:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/tag_list.html")
        self.assertIn("tag_list", response.context)
        self.assertEqual(len(response.context["tag_list"]), 1)
        self.assertEqual(response.context["tag_list"][0].name, "urgent")


class TagCreateViewTest(TestCase):

    def test_tag_create_view(self):
        response = self.client.post(
            reverse("app:tag-create"),
            {"name": "important"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("app:tag-list"))
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.first().name, "important")


class TagUpdateViewTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="urgent")

    def test_tag_update_view(self):
        response = self.client.post(
            reverse("app:tag-update", args=[self.tag.pk]), {"name": "updated"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("app:tag-list"))
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "updated")


class TagDeleteViewTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="urgent")

    def test_tag_delete_view(self):
        response = self.client.post(reverse(
            "app:tag-delete",
            args=[self.tag.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("app:tag-list"))
        self.assertEqual(Tag.objects.count(), 0)


class ToggleTaskStatusTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title="Task 1", deadline=date(2024, 6, 1), is_done=False
        )

    def test_toggle_task_status(self):
        response = self.client.post(
            reverse("app:toggle-task-status", args=[self.task.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("app:index"))
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)
