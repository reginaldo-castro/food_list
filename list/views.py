from django.shortcuts import render
from .models import Category

def index(request):
    category = Category.objects.order_by('-descricao')
    context = {'categoy': category}
    return render(request, 'category/index.html', context)