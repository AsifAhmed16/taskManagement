from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Task


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        label='Due date',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('author', 'created_date', 'updated_date')
