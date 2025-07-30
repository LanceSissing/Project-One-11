from django.http import JsonResponse
def get_models_for_make(request):
    from marketplace.models import Item
    make = request.GET.get('make', '')
    models = Item.objects.filter(make__iexact=make).values_list('model_name', flat=True).distinct()
    models = [m for m in models if m]
    return JsonResponse({'models': models})
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
    query = request.GET.get('q', '')
    make = request.GET.get('make', '')
    model = request.GET.get('model', '')
    year = request.GET.get('year', '')
    items = Item.objects.all()
    if make:
        items = items.filter(make__iexact=make)
    if model:
        items = items.filter(model_name__iexact=model)
    if year:
        items = items.filter(year__iexact=year)
    if query:
        from django.db.models import Q
        items = items.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(price__icontains=query)
        )
    items = items.order_by('-created_at')
    # Get distinct values for dropdowns
    makes = Item.objects.values_list('make', flat=True).distinct().exclude(make__isnull=True).exclude(make__exact='')
    models = Item.objects.values_list('model_name', flat=True).distinct().exclude(model_name__isnull=True).exclude(model_name__exact='')
    years = Item.objects.values_list('year', flat=True).distinct().exclude(year__isnull=True).exclude(year__exact='')
    return render(request, 'home.html', {
        'items': items,
        'query': query,
        'make': make,
        'model': model,
        'year': year,
        'makes': makes,
        'models': models,
        'years': years,
    })
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
