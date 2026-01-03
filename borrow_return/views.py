from django.shortcuts import render

def borrow_book(request):
    return render(request, 'borrow/borrow_book.html')

def return_book(request):
    return render(request, 'borrow/return_book.html')
