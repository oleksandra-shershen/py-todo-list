from django.test import TestCase
from app.models import Tag, Task
from datetime import date


class TagModelTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name="urgent")
        self.tag2 = Tag.objects.create(name="important")

    def test_tag_creation(self):
        tag = Tag.objects.create(name="new_tag")
        self.assertEqual(tag.name, "new_tag")
        self.assertTrue(isinstance(tag, Tag))
        self.assertEqual(str(tag), tag.name)

    def test_tag_ordering(self):
        tags = Tag.objects.all()
        self.assertEqual(tags[0].name, "important")
        self.assertEqual(tags[1].name, "urgent")


class TaskModelTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name="urgent")
        self.tag2 = Tag.objects.create(name="important")
        self.task1 = Task.objects.create(
            title="Task 1", deadline=date(2024, 6, 1), is_done=False
        )
        self.task1.tags.add(self.tag1, self.tag2)
        self.task2 = Task.objects.create(
            title="Task 2", deadline=date(2024, 7, 1), is_done=True
        )

    def test_task_creation(self):
        task = Task.objects.create(
            title="New Task", deadline=date(2024, 8, 1), is_done=False
        )
        self.assertEqual(task.title, "New Task")
        self.assertFalse(task.is_done)
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(str(task), task.title)

    def test_task_ordering(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

    def test_task_tags(self):
        task = Task.objects.get(title="Task 1")
        self.assertEqual(task.tags.count(), 2)
        self.assertIn(self.tag1, task.tags.all())
        self.assertIn(self.tag2, task.tags.all())
