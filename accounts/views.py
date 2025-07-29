from django.shortcuts import get_object_or_404
def edit_item(request, item_id):
    from marketplace.models import Item, ItemImage
    item = get_object_or_404(Item, id=item_id, owner=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            updated_item = form.save()
            # Handle new images
            images = request.FILES.getlist('images')
            for idx, image in enumerate(images):
                if idx < 6:
                    ItemImage.objects.create(item=updated_item, image=image)
            return redirect('account')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'item': item})
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ItemForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect
from marketplace.models import Item

from marketplace.models import Item

def home(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'items': items})
def item_detail(request, item_id):
    from marketplace.models import Item
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_detail.html', {'item': item})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')  # Redirect to account page after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def account(request):
    items = Item.objects.filter(owner=request.user)
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            new_item = item_form.save(commit=False)
            new_item.owner = request.user
            new_item.save()
            images = request.FILES.getlist('images')
            for idx, image in enumerate(images):
                if idx < 6:
                    from marketplace.models import ItemImage
                    ItemImage.objects.create(item=new_item, image=image)
            return redirect('account')
    else:
        item_form = ItemForm()
    return render(request, 'account.html', {'item_form': item_form, 'items': items})

@csrf_protect
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'registration/logout.html')
def delete_item_image(request, image_id):
    from marketplace.models import ItemImage
    image = get_object_or_404(ItemImage, id=image_id, item__owner=request.user)
    item_id = image.item.id
    image.delete()
    return redirect('edit_item', item_id=item_id)
