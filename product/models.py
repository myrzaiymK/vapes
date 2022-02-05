from django.db import models


class Product(models.Model):
    title = models.CharField(max_length = 25)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        blank=True
    )
    def __str__(self) -> str:
        return f"{self.title} {self.price}"
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email =models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f"{self.name} {self.phone}"


class Cart(models.Model):
    product_id = models.ForeignKey(Product,verbose_name='Товар', on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)

    def save(self, *args, **kwargs):
        self.final_price = self.number * self.product_id.price
        super().save(*args, **kwargs)

