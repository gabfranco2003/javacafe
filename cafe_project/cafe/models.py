from django.db import models
from django.utils.text import slugify 
from django.contrib.auth.models import User

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('coffee', 'Coffee'),
        ('tea', 'Tea'),
        ('juices', 'Juices'),
        ('pastries', 'Pastries'),
        ('sandwich', 'Sandwich'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  
    price = models.DecimalField(max_digits=6, decimal_places=2)  
    description = models.TextField()
    image = models.URLField(max_length=2080)  # Image field
    # Remove any other fields that may conflict with the image field
    slug = models.SlugField(unique=True, blank=True)  # Optional if you're not using slugs
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    
    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name if self.name else "No Name Provided"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(MenuItem, self).save(*args, **kwargs)
        
class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Optional description field
    name = models.CharField(max_length=200, blank=True, null=True)  # Optional name field
    image = models.URLField(max_length=2080)  # Using URLField for the image
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.URLField(max_length=2080, blank=True, null=True)

    def __str__(self):
        return self.title or "Untitled Carousel Item"
    
class Review(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Rating from 1 to 5
    comment = models.TextField()  # Review comment
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when review is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when review is modified
    helpful_count = models.PositiveIntegerField(default=0)  # Counter for helpful reviews

    def clean(self):
        """
        Ensure the rating is between 1 and 5.
        """
        if not (1 <= self.rating <= 5):
            raise ValidationError("Rating must be between 1 and 5.")

    class Meta:
        ordering = ['-created_at']  # Order by most recent first

    def __str__(self):
        return f"Review for {self.menu_item.name} by {self.user.username}"

    def mark_helpful(self):
        """
        Increment the helpful count when a review is marked helpful.
        """
        self.helpful_count += 1
        self.save()