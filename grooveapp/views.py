# from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required


def index(req):
    return render(req, 'grooveapp/index.html', {
    		'text': 'Groove Story'
    	})
def home(req):
    return render(req, 'grooveapp/home.html', {})


# @login_required
# def home(request):
#     return render(request, 'grooveapp/home.html')