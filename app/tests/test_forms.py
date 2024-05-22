from django.test import TestCase
from app.forms import TagForm, TaskForm
from app.models import Tag
from datetime import date


class TagFormTest(TestCase):

    def test_valid_tag_form(self):
        form_data = {"name": "urgent"}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())
        tag = form.save()
        self.assertEqual(tag.name, "urgent")

    def test_invalid_tag_form(self):
        form_data = {"name": ""}
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class TaskFormTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name="urgent")
        self.tag2 = Tag.objects.create(name="important")

    def test_valid_task_form(self):
        form_data = {
            "title": "Test Task",
            "deadline": date(2024, 6, 1),
            "is_done": False,
            "tags": [self.tag1.id, self.tag2.id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        task = form.save()
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.deadline, date(2024, 6, 1))
        self.assertFalse(task.is_done)
        self.assertIn(self.tag1, task.tags.all())
        self.assertIn(self.tag2, task.tags.all())

    def test_invalid_task_form(self):
        form_data = {
            "title": "",
            "deadline": date(2024, 6, 1),
            "is_done": False
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_task_form_with_invalid_tags(self):
        form_data = {
            "title": "Test Task",
            "deadline": date(2024, 6, 1),
            "is_done": False,
            "tags": ["invalid_tag_id"],
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("tags", form.errors)

    def test_task_form_with_no_tags(self):
        form_data = {
            "title": "Test Task",
            "deadline": date(2024, 6, 1),
            "is_done": False,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        task = form.save()
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.deadline, date(2024, 6, 1))
        self.assertFalse(task.is_done)
        self.assertEqual(task.tags.count(), 0)
