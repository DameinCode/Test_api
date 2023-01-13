from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='profiles/')

class Order(models.Model):
    STATUS_CHOICES = (
        ('sent', 'sent'),
        ('contact soon', 'contact soon'),
        ('accepted', 'accepted'),
        ('cancelled', 'cancelled'),
    )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
