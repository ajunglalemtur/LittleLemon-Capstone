from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet
from . import views


router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),   # API endpoints at /restaurant/api/
    path('', views.index, name='index'),  # index page at /restaurant/
]
