from django import forms

from tasks.models import TodoItem


class AddTaskForm(forms.Form):
    description = forms.CharField(max_length=64, label="")


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('description', 'priority')
        labels = {"description": "описание", "priority": ""}

class TodoItemExportForm(forms.Form):
    prio_high = forms.BooleanField(label='высокая важность', initial=True, required=False)
    prio_med = forms.BooleanField(
        label='средняя важность', initial=True, required=False)
    prio_low = forms.BooleanField(
        label='низкая важность', initial=False, required=False)
