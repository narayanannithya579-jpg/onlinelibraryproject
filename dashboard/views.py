from django.shortcuts import render

def dashboard_home(request):
    return render(request, 'dashboard.html')
def home(request):
    return render(request, 'home.html')