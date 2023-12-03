from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/task_list/', TaskApiList.as_view()),
    # path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    # path('api/v1/task_delete/<int:pk>/', TaskApiDelete.as_view()),
]