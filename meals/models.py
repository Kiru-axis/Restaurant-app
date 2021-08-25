from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural ="categories"



class Meals(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    people = models.PositiveBigIntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    preperation_time=models.IntegerField()
    image=models.ImageField(upload_to="meals/")
    slug=models.SlugField(blank=True,null=True)
    
    # slugify the name
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals,self).save(*args, **kwargs)
    # call
    def __str__(self):
        return f"{self.name}"

    # meta
    class Meta:
        verbose_name = "meal"
        verbose_name_plural ="meals"


