from django.shortcuts import render

def sell_book(request):
    return render(request, 'sell/sell_book.html')
