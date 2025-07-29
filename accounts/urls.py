from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('item/<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('item/image/<int:image_id>/delete/', views.delete_item_image, name='delete_item_image'),
    path('logout/', views.logout_view, name='logout'),
]
