from rest_framework import viewsets
from django.shortcuts import render  # Import render for the index view
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# API viewsets
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Web page view for home page
def index(request):
    return render(request, 'index.html', {})
