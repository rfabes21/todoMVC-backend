from tastypie.resources import ModelResource
from .models import TodoItem


class TodoItemResource(ModelResource):
    class Meta:
        queryset = TodoItem.objects.all()
