from django.contrib.auth import views as auth_views  # Add this import
from django.urls import path
from . import views

urlpatterns = [
    # Web views
    path('', views.home, name='home'),  # Homepage
    path('about/', views.about, name='about'),  # About page
    path('menu/', views.menu, name='menu'),  # Menu page
    path('menu/<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),  # Detail of individual menu item
    path('profile/', views.profile_view, name='profile'),  # Profile page
    # Combined List and Create view for MenuItem
    path('menu/create/', views.MenuItemListCreateView.as_view(), name='menu_item_create'),  # This should use MenuItemListCreateView
    
    # If you have separate views for updating and deleting
    path('menu/<int:pk>/update/', views.MenuItemUpdateView.as_view(), name='menu_item_update'),
    path('menu/<int:pk>/delete/', views.MenuItemDeleteView.as_view(), name='menu_item_delete'),

    # Add other URLs as needed
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Use auth_views here
]
