from django.shortcuts import render

def notifications_page(request):
    return render(request, 'notifications/notifications.html')
