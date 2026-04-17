from django import forms

from todolist.models import Tags, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "content": forms.TextInput(),
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
            ),
        }
