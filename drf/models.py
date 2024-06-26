from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title
