from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet, MenuItemsView, SingleMenuItemView

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),  # include router without 'api/' prefix here
    path('menu-items/', MenuItemsView.as_view(), name='menu-items'),  # fixed to menu-items
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
]

