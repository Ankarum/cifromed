from django import forms

from django.contrib.auth.models import User

from .models import Profile

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('middle_name', 'birthday', 'sex', 'city', 'postcode', 'region', 'street',
		'housing', 'structure', 'house', 'apartment', 'mobile_phone', 'company', 'profession',
		'position', 'insurance_policy', 'SNILS', 'passport')

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ( 'email', 'first_name', 'last_name')


