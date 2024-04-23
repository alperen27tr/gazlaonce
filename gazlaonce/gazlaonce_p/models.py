from django.db import models
from django.contrib.auth.models import AbstractUser

                    
class base_category(models.Model):
    base_category_names=models.CharField(max_length=200,null = True)
    is_active=models.CharField(max_length=10,null=True)
    date_upload=models.DateTimeField(null=True)
    date_update=models.DateTimeField(null=True)

    def __str__(self):
        return self.base_category_names
    
class categories(models.Model):
    categoriesName=models.CharField(max_length=50,null=True)
    base_categories = models.ForeignKey(base_category, on_delete=models.CASCADE,null=True)
    is_active=models.CharField(max_length=10,null=True)
    date_upload=models.DateTimeField(null=True)
    date_update=models.DateTimeField(null=True)

    def __str__(self):
        return self.categoriesName 
     

class base_videos(models.Model):
    title=models.CharField(max_length=200)
    link=models.URLField()
    categories = models.ForeignKey(categories, on_delete=models.CASCADE,null=True)
    base_categories = models.ForeignKey(base_category, on_delete=models.CASCADE,null=True)
    is_active=models.BooleanField(null=True)
    date_upload=models.DateTimeField(null=True)
    date_update=models.DateTimeField(null=True)

    def __str__(self):
        return self.title
    
