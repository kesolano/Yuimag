from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users_listt(models.Model):

    email = models.EmailField()
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    subscribed = models.BooleanField(default=False)


    def __str__(self):
        text = "{0} ({1})"

        return text.format(self.username, self.email)


class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
