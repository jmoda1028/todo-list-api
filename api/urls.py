from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('todos', views.TodoView)

urlpatterns = [
    path('count_pending_tasks/', views.CustomView.count_pending_tasks),
    path('', include(router.urls)),   
]
