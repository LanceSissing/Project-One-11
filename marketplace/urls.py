from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:item_id>/send_message/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='messages_inbox'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
    path('account/edit/', views.edit_account_view, name='edit_account'),
    path('messages/<int:message_id>/reply/', views.message_reply, name='message_reply'),
    path('sent/', views.sent_messages, name='sent_messages'),
]
