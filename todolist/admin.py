from django.contrib import admin

from todolist.models import Task, Tags


admin.site.register(Task)
admin.site.register(Tags)
