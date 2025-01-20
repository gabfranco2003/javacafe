from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('coffee', 'Coffee'),
        ('tea', 'Tea'),
        ('pastries', 'Pastries'),
        ('sandwich', 'Sandwich'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.URLField(max_length=2080)  # Keep URLField for image URLs

    def __str__(self):
        return self.name

class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.URLField(max_length=2080)  # Keep URLField for image URLs
    
    def __str__(self):
        return self.title
