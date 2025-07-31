from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:item_id>/send_message/', views.send_message, name='send_message'),
]
