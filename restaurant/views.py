from datetime import datetime

from django.core import serializers
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import MenuSerializer


#
# API views
#
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()


#
# Page views
#
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html')


def reservations(request: HttpRequest) -> HttpResponse:
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'reservations.html', {"bookings": booking_json})
