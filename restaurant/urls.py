from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet, MenuItemsView, SingleMenuItemView

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('menu/items', MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view(), name='single-menu-item'),
]
