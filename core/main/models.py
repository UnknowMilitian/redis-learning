from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField("Some title", max_length=250)

    def __str__(self):
        return self.title


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="item"
    )
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description", blank=True)

    def __str__(self):
        return self.title
