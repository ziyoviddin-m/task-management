from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# class TaskApiList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#

# class TaskApiDelete(generics.RetrieveDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
