from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Message
# from django.contrib.auth.decorators import login_required


def index(req):
    return render(req, 'grooveapp/index.html', {
    		'text': 'Groove Story'
    })

def lobby(req):
    if req.method == 'POST':
        message = Message(text = req.POST['message'], author=req.user)
        message.save()
        return redirect('/lobby/')

    return render(req, 'grooveapp/lobby.html', {
        'messages': Message.objects.all(),
        'user': req.user
    })

def get_messages(req):
    return JsonResponse([
        {
            'author': m.author.username,
            'text': m.text,
            'time': m.time
        } for m in Message.objects.all()
    ], safe=False)


# def home(req):
#     return render(req, 'grooveapp/home.html', {})


# @login_required
# def home(request):
#     return render(request, 'grooveapp/home.html')