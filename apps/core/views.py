from django.shortcuts import render

def mainpage(request):
    return render(request, 'core/mainpage.html')

def about(request):
    return render(request, 'core/about.html')

def info(request):
    return render(request, 'core/info.html')
