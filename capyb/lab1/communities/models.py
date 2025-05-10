from django.db import models

class Community(models.Model):
    title = models.CharField(max_length=255, default="Без названия")
    description = models.TextField()
    slug = models.SlugField(unique=True)
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    
    def __str__(self):
        return self.title
