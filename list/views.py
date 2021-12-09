from django.shortcuts import get_object_or_404, redirect, render

from list.form import CategoryForm
from .models import Category
from django.views.generic import ListView, DetailView

def category(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'category/index.html', context)

def category_detail(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'category/detail.html', {'category': category})

def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    form = CategoryForm()

    return render(request, 'category/create.html', {'form': form})

def category_edit(request, id):
    category = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category')
    return render(request, 'category/edit.html', {'form': form})

def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('category')
    return render(request, 'category/confirm_delete.html', {'category': category})


#senha de admin
#reginaldo
#dev01