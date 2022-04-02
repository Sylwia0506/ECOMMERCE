from django.db import models


class Category(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = "categories"
