from django.urls import path
from . import views

urlpatterns = [
    path('sell/', views.sell_book, name='sell_book'),
]
