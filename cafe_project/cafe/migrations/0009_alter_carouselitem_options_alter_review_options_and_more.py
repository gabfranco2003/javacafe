# Generated by Django 5.1.4 on 2025-01-21 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_alter_menuitem_category_alter_menuitem_price_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carouselitem',
            options={},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='button_link',
            field=models.URLField(blank=True, max_length=2080, null=True),
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='button_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='review',
            name='helpful_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_images/'),
        ),
    ]
