from django.contrib.auth import login, authenticate
from django.shortcuts import  render , HttpResponse, redirect
from apps.users.forms import RegistrationForm
from apps.users.models import User

#Al tener un User Custom, debemos utilizar el get_user_model para acceder a el.

def user_detail(request, pk):
    user = User.objects.get(pk = pk)

    return render(request, 'users/user_detail.html', {
        'user' : user
    })

def register_view(request, *args, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    elif (request.method == 'POST'):
        print("hello")
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            login(request,account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            else:
                pass
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html',context)