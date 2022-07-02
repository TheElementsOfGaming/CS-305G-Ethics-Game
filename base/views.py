from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def settings(request):
    return render(request, 'settings.html')

def mainpage(request):
	return render(request, 'mainpage.html')