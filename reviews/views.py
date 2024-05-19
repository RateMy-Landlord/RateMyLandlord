from django.shortcuts import render, get_object_or_404
from .models import Reviews
from landlord.models import Landlord

def landlord_detail(request, landlord_id):
    landlord = get_object_or_404(Landlord, pk=landlord_id)
    reviews = Reviews.objects.filter(lord=landlord)
    return render(request, 'landlord_detail.html', {'landlord': landlord, 'reviews': reviews})
