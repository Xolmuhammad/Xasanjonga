from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from user.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    icon = models.TextField()

    def __str__(self):
        return self.name


class Additional(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Nomi")
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="Matni")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    additionals = models.ManyToManyField(Additional, verbose_name="Qo'shimcha", related_name="products")
    preparation_time = models.IntegerField(verbose_name="Tayyorlanish vaqti")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Kategoriyasi",
                                 related_name="products")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot "
        verbose_name_plural = 'Mahsulotlar'
        ordering = ['-name']

    def get_image(self):
        product_images = self.images.all()
        if product_images:
            return product_images[0].image.url
        else:
            return "https://img.freepik.com/free-vector/404-error-design-with-donut_23-2147739030.jpg?semt=ais_rp_50_assets&w=740&q=80"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.product.name}"


class Comment(models.Model):
    text = models.CharField(max_length=500)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text}"


class Order(models.Model):
    PAYMENT_TYPE = {
        'cash': 'Cash',
        'card': 'Card'
    }

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    created = models.DateTimeField()
    payment_type = models.CharField(max_length=4, choices=PAYMENT_TYPE)
    time_delivery = models.DateTimeField()
    delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address