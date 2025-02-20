from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    
    if request.method == 'POST':
        add_book = Bookform(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_cat = Categoryform(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    context={
        'categors':Category.objects.all(),
        'Books':Book.objects.all(),
        'forms':Bookform(),
        'cat':Categoryform(),
        'allbooks':Book.objects.filter(active=True).count(),
        'booksold':Book.objects.filter(status='sold').count(),
        'bookrental':Book.objects.filter(status='rental').count(),
        'bookavaible':Book.objects.filter(status='avaible').count(),
    }
    return render(request,'pages/index.html',context)

def books(request):
    if request.method == 'POST':
        add_book = Bookform(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_cat = Categoryform(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    context={
        'categors':Category.objects.all(),
        'Books':search,
        'cat':Categoryform(),
    }
    return render(request,'pages/books.html',context)

def delete(request,id):
    book_delete = Book.objects.get(id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')

def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = Bookform(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = Bookform(instance=book_id)
    context = {
        'form':book_save
    }
    return render(request,'pages/update.html',context)
