from django.db import models

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
