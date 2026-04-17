from django.db import models


class Task(models.Model):
    content = models.TextField(
        max_length=255,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    marked = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        "Tags",
        related_name="tasks"
    )

    class Meta:
        ordering = ["marked"]


class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
