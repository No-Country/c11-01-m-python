from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from apps.account.models import Account


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Obligatorio! Necesita una direccion de correo valida.')

	class Meta:
		model = Account
		fields = ('email', 'username', 'direction','firstname','lastname','phone','password1', 'password2', )

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" Ya esta en uso.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('El username "%s" ya esta en uso.' % username)