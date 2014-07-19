from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

from .models import TodoItem


class TodoItemResource(ModelResource):
    class Meta:
        queryset = TodoItem.objects.all()
        authentication = Authentication()
        authorization = Authorization()
