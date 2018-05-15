from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class tag(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class profile(models.Model):
    profile_photo = models.ImageField(upload_to ='images/')
    Bio = models.CharField(max_length =30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_photo



class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =60)
    caption = HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image

    def save_editor(self):
        self.save()
    class Meta:
        ordering = ['image']


    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
