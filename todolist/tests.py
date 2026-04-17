from django.test import TestCase
from django.urls import reverse

from todolist.models import Task, Tags


class ListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag_1 = Tags.objects.create(name='test')
        cls.tag_2 = Tags.objects.create(name='test2')
        cls.task_1 = Task.objects.create(
            content="test",
            deadline="2026-08-13 12:00",
        )
        cls.task_2 = Task.objects.create(
            content="test2",
            marked=True,
        )
        cls.task_1.tags.add(cls.tag_1)
        cls.task_2.tags.add(cls.tag_2)

    def test_task_list_view(self):
        response = self.client.get(reverse("todolist:task-list"))
        self.assertEqual(
            list(response.context["tasks"]),
            list(Task.objects.all()),
        )

    def test_tags_list_view(self):
        response = self.client.get(reverse("todolist:tag-list"))
        self.assertEqual(
            list(response.context["tags"]),
            list(Tags.objects.all()),
        )
