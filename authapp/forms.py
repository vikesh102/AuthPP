from django import forms
from authapp.models import Userinfo


class UserLoginForm(forms.ModelForm):
	class Meta:
		model=Userinfo
		fields=['Email','Password']
