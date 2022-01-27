"""scmf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from client.api import viewsets as clientsViewSets
from doctor.api import viewsets as doctorsViewSets
from drugstore.api import viewsets as drugstoresViewSets
from drugstore_orders.api import viewsets as ordersViewSets
from appointment.api import viewsets as appointmentViewsSets

route = routers.DefaultRouter()
route.register(r'clients', clientsViewSets.ClientViewSet, basename="Client")
route.register(r'doctor', doctorsViewSets.DoctorViewSet, basename="Doctor")
route.register(r'drugstore', drugstoresViewSets.DrugstoreViewSet, basename="Drugstore")
route.register(r'order', ordersViewSets.DrugstoreOrderViewSet, basename='Order')
route.register(r'appointment', appointmentViewsSets.AppointmentViewSet, basename='Appointment')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
