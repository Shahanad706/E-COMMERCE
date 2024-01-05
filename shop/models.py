from django.db import models
from django.urls import reverse
# Create your models here.
class categ(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    # class meta:
    #     ordering=('name',)
    #     verbose_name='category'
    #     verbose_name_plural='categories'

    def get_url(self):
        return reverse('product_cat',args=[self.slug])

class products(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.category,self.slug])

    def __str__(self):
        return '{}'.format(self.name)