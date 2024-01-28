from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=225)
    added_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# Модель для поиска статей
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='articles', blank=True)
    category_name = models.ManyToManyField(Category, null=True)


def __str__(self):
        return self.title


