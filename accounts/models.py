

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_buyer = models.BooleanField(default=True, verbose_name='Buyer')
    is_seller = models.BooleanField(default=True, verbose_name='Seller')
    is_business = models.BooleanField(default=False, verbose_name='Business')
    # Add more custom fields as needed
