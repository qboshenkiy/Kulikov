from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length=300)
    image = models.ImageField(upload_to="media/image")

    def __str__(self):
        return self.title