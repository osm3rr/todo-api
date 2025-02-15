from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework import generics

# Create your views here.
class ListTodoItem(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
