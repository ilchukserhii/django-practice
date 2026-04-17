from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from todolist.forms import TaskForm
from todolist.models import Task, Tags


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    queryset = Task.objects.prefetch_related("tags").distinct()


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:task-list")


class TagsListView(generic.ListView):
    model = Tags
    context_object_name = "tags"


class TagsCreateView(generic.CreateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagsUpdateView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagsDeleteView(generic.DeleteView):
    model = Tags
    success_url = reverse_lazy("todolist:tag-list")


class ToogleMarkTask(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.marked = not task.marked
        task.save()
        return HttpResponseRedirect(reverse_lazy("todolist:task-list"))
