from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Message, TreeCardGame, MakeChat
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(req):
    return render(req, 'grooveapp/index.html', {
    		'text': 'Groove Story'
    })

def profile(req):
    return render(req, 'grooveapp/profile.html', {})

def story(req):
    return render(req, 'grooveapp/stories.html', {
     "story" : TreeCardGame.objects.order_by('?')[0:1],
    })

def infostories(req):
    return render(req, 'grooveapp/infostories.html', {})


def makechat(req):
    if req.method == 'POST':
        chat = MakeChat(title = req.POST['title'], names = req.POST['chatname'], lobbyid = 'lobby')
        chat.save()
        chat.id
        # return redirect('')
    return render(req, 'grooveapp/makechat.html', {
    })


def lobby(req, name):
    if req.method == 'POST':
        message = Message(
        text = req.POST['message'],
        author=req.user)
        message.save()
        return redirect('/lobby/')

    return render(req, 'grooveapp/lobby.html', {
        'messages' : Message.objects.all(),
        'user' : req.user,
    })

def get_messages(req):
    return JsonResponse([
        {
            'author': m.author.username,
            'text': m.text,
            'time': m.time
        } for m in Message.objects.all()
    ], safe=False)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'grooveapp/signup.html', {'form': form})
