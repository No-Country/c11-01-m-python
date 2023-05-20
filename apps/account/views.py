from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from apps.account.models import Account 
from django.conf import settings
from apps.account.forms import RegistrationForm, AccountAuthenticationForm


def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse('Ya estas autenticado con: ' + str(user.email))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
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
	# user_id = kwargs.get('user_id')
	# account = Account.objects.get(pk = user_id)
	# user = request.user
	# if user.is_authenticated and user != account:
	# 	return redirect('/')
	# elif not user.is_authenticated:
	# 	return redirect('/account/login')
	# return render(request, 'account/account.html', {
	# 	'account': account
	# })

	context = {}
	user_id = kwargs.get('user_id')
	try:
		account = Account.objects.get(pk = user_id)
	except Account.DoesNotExist:
		return HttpResponse('El usuario no existe.')
	if account:
		context['id'] = account.id
		context['email'] = account.email
		context['firstname'] = account.firstname
		context['lastname'] = account.lastname
		context['direction'] = account.direction
		context['phone'] = account.phone
		context['hide_email'] = account.hide_email

		#Revisaremos si estas en tu perfil o en el perfil de otra persona
		is_self = True
		user = request.user
		#Veremos si esta logeado, pero no es la misma persona
		if user.is_authenticated and user != account:
			return redirect('/')
		elif not user.is_authenticated:
			return redirect('/account/login')
		
		context['is_self'] = is_self
		context['BASE_URL'] = settings.BASE_URL
		return render(request, 'account/account.html', {
			'account' : context
		})
	