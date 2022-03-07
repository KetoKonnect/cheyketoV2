from email.mime import image
from django.db import models
from django.http import HttpResponse
from django.urls import reverse
# Create your models here.

# Items that are published
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(published=True)

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, blank=True, default=None)
    name = models.CharField('Product Name', max_length=250, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, default=None, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField('Product Description', blank=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    quantity = models.IntegerField('Quantity Available')
    published = models.BooleanField('Published')
    code = models.CharField('LookUP Code', max_length=500)
    
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)

    #model managers
    objects = models.Manager() # Default Manager
    on_shelf = PublishedManager() # Manager for items that are published

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class Thumbnail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='thumbnails')
    # name = models.CharField('Name')
    is_primary = models.BooleanField('Default', default=True)
    upload = models.ImageField('Image File', upload_to='thumbnails/%Y/%m/%d/')

    def __str__(self):
        return self.upload.name

