from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
    first_author_name = models.CharField(max_length=50)
    last_author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_author_name + ' ' + self.last_author_name

class GrStory(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Message(models.Model):
    text = models.TextField(max_length=600)
    time = models.DateField(auto_now=True)
    author = models.ForeignKey(User)

class TreeCardGame(models.Model):
    categories = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    whatHappended = models.CharField(max_length=50)

class MakeChat(models.Model):
    title = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    lobbyid = models.CharField(max_length=100)

