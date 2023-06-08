from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from apps.account.models import Account 
from django.conf import settings
from apps.account.forms import RegistrationForm, AccountAuthenticationForm
from apps.store.models import Order
import re


def register_view(request, *args, **kwargs):
	user = request.user

	#regex de password
	#fin regex password

	if user.is_authenticated: 
		return HttpResponse('Ya estas autenticado con: ' + str(user.email))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		validation_pass = request.POST.get('password1')
		if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{8,25}$", validation_pass):
			if form.is_valid():
				form.save()
				email = form.cleaned_data.get('email').lower()
				raw_password = form.cleaned_data.get('password1')
				account = authenticate(email=email, password=raw_password)
				login(request, account)
				destination = kwargs.get('next')
				if destination:
					return redirect(destination)
				return redirect('/')
			else:
				context['registration_form'] = form
		else:
			print('password no valido')
			return render(request, 'account/register.html')

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)

#Logut
#Usamos la funcion de django.contrib.auth logout
def logout_view(request):
	logout(request)
	return redirect('/')

#Login
def login_view(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect('/')

	destination = get_redirect_if_exists(request)
	print("destination: " + str(destination))

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				if destination:
					return redirect(destination)
				return redirect('/')

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, 'account/login.html', context)


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get('next'):
			redirect = str(request.GET.get('next'))
	return redirect

#Pagina del usuario
def account_view(request, *args, **kwargs):
	user_id = kwargs.get('user_id')
	account = Account.objects.get(pk = user_id)
	user = request.user
	if user.is_authenticated and user != account:
		return redirect('/')
	elif not user.is_authenticated:
		return redirect('/account/login')
	
	#Miramos las ordenes que tiene dicho usuario
	orders = Order.objects.filter(created_by = user_id)
	return render(request, 'account/account.html', {
		'account': account,
		'orders' : orders
	})

	