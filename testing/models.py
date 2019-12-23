from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=True)
    features = models.BooleanField(default=False)

    ##For making urls dynamic..

    ##Method 1
    # def get_absolute_url(self):
    #     return f"/product/{self.prod_id}/"


    ##Method 2
    def get_absolute_url(self):
        return reverse("prodDetail", kwargs={'prod_id':self.id})




class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField()

    def __str__(self):
        return self.title
