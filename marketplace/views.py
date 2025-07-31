from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, Message
from .forms import MessageForm

@login_required
def send_message(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    recipient = item.owner
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.item = item
            message.save()
            return redirect('messages_inbox')  # You can adjust this redirect as needed
    else:
        form = MessageForm()
    return render(request, 'marketplace/send_message.html', {'form': form, 'item': item, 'recipient': recipient})
from django.shortcuts import render

# Create your views here.
