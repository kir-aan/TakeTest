from django import forms
from .models import TestInfo
from crispy_forms.helper import FormHelper

class TestForm(forms.ModelForm):

    class Meta:
        model = TestInfo
        fields = ['TestName', 'MaxMarks', 'TimeDuration', 'PosMarks', 'NegMarks', 'InputTextFile']

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
