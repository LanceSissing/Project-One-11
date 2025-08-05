from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, Message
from .forms import MessageForm

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'marketplace/inbox.html', {'messages': messages})

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'marketplace/sent_messages.html', {'messages': messages})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id, recipient=request.user)
    if not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'marketplace/message_detail.html', {'message': message})

@login_required
def message_reply(request, message_id):
    original_message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.recipient = original_message.sender
            reply.item = original_message.item  # Optional: link to the same item
            reply.save()
            return redirect('messages_inbox')
    else:
        form = MessageForm(initial={
            'subject': f"Re: {original_message.subject}",
        })
    return render(request, 'marketplace/message_reply.html', {
        'form': form,
        'original_message': original_message,
    })

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

def edit_account_view(request):
    # Placeholder view for now
    return render(request, 'edit_account.html')

# Create your views here.
