from django.urls import path
from . import views



urlpatterns = [
    path('category', views.category, name="category"),
    path('category/new', views.category_new, name="category_new"),
    path('category/edit/<int:id>', views.category_edit, name='category_edit'),
    path('category/delete/<int:id>', views.category_delete, name="category_delete"),
    path('category/<int:id>', views.category_detail, name="category_detail"),
]
