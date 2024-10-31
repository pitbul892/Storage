from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, TypeViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('types', TypeViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
