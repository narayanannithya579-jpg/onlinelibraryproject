from django.urls import path
from . import views  # import your views from accounts app

urlpatterns = [
    # Example routes, change according to your views
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
