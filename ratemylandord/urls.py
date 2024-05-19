"""
URL configuration for ratemylandord project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
import ratemylandord.views
import landlord.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ratemylandord.views.index,name="index"),
    path('search/', ratemylandord.views.search_landlords_by_address, name='search_landlords_by_address'),
    path('add_landlord/', landlord.views.add_landlord, name='add_landlord'),
    path('landlord/<int:landlord_id>/', reviews.views.landlord_detail, name='landlord_detail'),
    path('add_review/<int:landlord_id>/', reviews.views.add_review, name='add_review'),
]
