from django.db import models


class Category(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = "categories"

        def __str__(self):
            return self.name


class Product(models.Model):
    category = model.ForeginKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    created_by = models.ForeginKey(
        User, on_delete=models.CASCADE, related_name="product_creator"
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    slug = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(add_now=True)
    updated = models.DataTimeField(add_now=True)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-created",)

    def __str__(self):
        return self.title
