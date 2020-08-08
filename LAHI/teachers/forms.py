from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from main.models import MediaFile


class NewStudentForm(UserCreationForm):
	# email = forms.EmailField(required=True)
    
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')

	def save(self, commit=True):
		user = super(NewStudentForm, self).save(commit=False)
		# user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class MediaForm(forms.ModelForm):
    class Meta:
        model= MediaFile
        fields= ["std", "subject", "file_type", "media"]

