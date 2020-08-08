from django import forms
from teachers.models import Student

class StudentAuthenticationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'phone']
