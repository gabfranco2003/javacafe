from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import MenuItem
from .forms import MenuItemForm

# Home view
def home(request):
    return render(request, 'cafe/home.html')  # Ensure this template exists

# About view
def about(request):
    return render(request, 'cafe/about.html')  # Ensure this template exists

# Menu view
def menu(request):
    menu_items = MenuItem.objects.all()  # Retrieve all menu items
    return render(request, 'cafe/menu.html', {'menu_items': menu_items})  # Pass to template

def profile_view(request):
    # Profile view logic here
    return render(request, 'cafe/profile.html')

# Menu Item Detail view
def menu_item_detail(request, item_id):
    item = MenuItem.objects.get(id=item_id)  # Retrieve specific menu item by ID
    return render(request, 'cafe/menu_item_detail.html', {'item': item})  # Pass to template

# Combined List and Create view for MenuItem
class MenuItemListCreateView(ListView, CreateView):
    model = MenuItem
    template_name = 'cafe/menu_item_list_create.html'  # Ensure this template exists
    context_object_name = 'menu_items'  # This makes MenuItem objects available as 'menu_items' in the template
    form_class = MenuItemForm  # Ensure you have a form class for MenuItem

    # Success URL after the form is submitted successfully
    success_url = reverse_lazy('menu')  # Change this to the desired redirect URL

    def get_context_data(self, **kwargs):
        """
        Include the list of MenuItem objects and the form for creating a new MenuItem.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Add form to the context
        return context

    def form_valid(self, form):
        """
        Handle successful form submission and display a success message.
        """
        messages.success(self.request, "Menu item created successfully!")
        return super().form_valid(form)

    def get_queryset(self):
        """
        Retrieve all the MenuItem objects for the ListView.
        """
        return MenuItem.objects.all()

# MenuItem Update view
class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm  # This should be the form for updating a MenuItem
    template_name = 'cafe/menu_item_update.html'  # Ensure this template exists
    context_object_name = 'item'  # This makes the MenuItem instance available as 'item' in the template

    # Success URL after the update is successful
    success_url = reverse_lazy('menu')  # Redirect to the menu page after updating

    def form_valid(self, form):
        """
        Handle successful form submission and display a success message.
        """
        messages.success(self.request, "Menu item updated successfully!")
        return super().form_valid(form)


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'cafe/menu_item_confirm_delete.html'  # Ensure this template exists
    context_object_name = 'menu_item'  # Name of the object in the context

    # Redirect to a different page after deletion (e.g., the menu page)
    success_url = reverse_lazy('menu')

    def delete(self, request, *args, **kwargs):
        """
        Custom delete method to display a success message after deletion.
        """
        messages.success(self.request, "Menu item deleted successfully!")
        return super().delete(request, *args, **kwargs)