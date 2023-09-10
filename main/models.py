from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Chefs(models.Model):
    img = models.ImageField(upload_to='chefs/')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.title

class Restaurent(models.Model):
    img = models.ImageField(upload_to='gallery/')



class Special_menu(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='menu_s/')
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='menu/')
    text = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Testiminional(models.Model):
    text = models.TextField()
    img = models.ImageField(upload_to='cooker/')
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Blog(models.Model):
    img = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=255)
    date = models.DateField()
    text = models.TextField()

class Email(models.Model):
    email = models.TextField()


class About_link(models.Model):
    twitter = models.TextField()
    telegram = models.TextField()
    instagram = models.TextField()
    facebook = models.TextField()


class Address(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name



