# API для приема заказов на разработку сайтов
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    email = models.EmailField()
    birth_date = models.DateField(null=True, blank=True)
    image = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.email


class Application(models.Model):
    description = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default="Sent")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title

    # STATUS_CHOICES = (
    #     ('sent', 'sent'),
    #     ('contact soon', 'contact soon'),
    #     ('accepted', 'accepted'),
    #     ('cancelled', 'cancelled'),
    # )

# class Image(models.Model):
    # url = models.TextField(default='')
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)