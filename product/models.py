from django.db import models


class Product(models.Model):
    title = models.CharField(max_length = 25)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        blank=True
    )
    def __str__(self) -> str:
        return f"{self.title} {self.price}"
# Create your models here.
