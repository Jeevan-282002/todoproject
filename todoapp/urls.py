from django.urls import include, path
from rest_framework import routers
from .views import TodoItemViewSet

router = routers.DefaultRouter()
router.register(r'todoitems', TodoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
