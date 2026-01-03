from django.shortcuts import render

def donate_book(request):
    return render(request, 'donate/donate_book.html')
