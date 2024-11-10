from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    published = models.BooleanField(default=False)
