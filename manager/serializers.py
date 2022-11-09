from decimal import Decimal
from rest_framework import serializers
from .models import Product,Customer ,Collection, Review, Cart, CartItem
from django.db.models.aggregates import Count, Sum


