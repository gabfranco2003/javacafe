from django.shortcuts import render, get_object_or_404
from .models import MenuItem, CarouselItem

def home(request):
    # Fetching all menu items
    menu_items = MenuItem.objects.all()

    # Grouping menu items by category
    categories = ['coffee', 'tea', 'pastries', 'sandwich', 'ice_cream']
    grouped_items = {category: menu_items.filter(category=category) for category in categories}

    # Fetching items for the carousel
    carousel_items = CarouselItem.objects.all()

    # Limiting the number of featured items (3 from each category)
    featured_items = {}
    for category, items in grouped_items.items():
        featured_items[category] = items[:3]  # Only take the first 3 items per category

    context = {
        'grouped_items': grouped_items,   # All items grouped by category
        'featured_items': featured_items, # Only the first 3 items per category
        'carousel_items': carousel_items, # Items for the carousel
    }

    return render(request, 'cafe/home.html', context)

def about(request):
    """
    About page view.
    """
    return render(request, 'cafe/about.html')

def menu(request):
    menu_items = MenuItem.objects.all()
    categories = ['coffee', 'tea', 'pastries', 'sandwich']

    # Group the menu items by category and limit to 3 items per category
    grouped_items = {
        category: menu_items.filter(category=category)[:3]  # Limit to 3 items
        for category in categories
    }

    return render(request, 'cafe/menu.html', {'grouped_items': grouped_items})

def menu_item_detail(request, item_id):
    """
    Detailed view of a specific menu item.
    """
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'cafe/menu_item_detail.html', {'item': item})
