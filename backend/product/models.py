from django.db import models

from category.models import Category

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200)
    imagem = models.ImageField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")

    def __str__(self):
        return self.descricao

