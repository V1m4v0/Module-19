from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100, help_text='username аккаунта')
    balance = models.DecimalField(max_digits=7, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100, help_text='Game name')
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=30, help_text='Заголовок новости')
    content = models.TextField(help_text='Содержание новости')
    date = models.DateTimeField(auto_now_add=True)