from django.urls import path

from todolist.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    mark_tasks,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "<int:pk>/toggle-task/",
        mark_tasks,
        name="task-toggle"
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tag-create"),
    path(
        "tags/<int:pk>/update/",
        TagsUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagsDeleteView.as_view(),
        name="tag-delete"
    )
]


app_name = "todolist"
