from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique = True)
    role = models.CharField(max_length=5)

    def __str__(self):
        return self.name    

class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name = 'products')

    def __str__(self):
        return self.name

#------------------------------------------gamemanager------------------------------------------

class Game(models.Model):
    title = models.CharField(max_length = 40)
    genres = models.ManyToManyField("Genre", related_name = 'games')
    release_date = models.DateField()
    rating = models.FloatField()

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
    



