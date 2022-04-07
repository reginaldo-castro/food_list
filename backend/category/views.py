from rest_framework import generics
from .serializers import CategorySerializer
from .models import Category

# Create your views here.
class CategoryList(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
