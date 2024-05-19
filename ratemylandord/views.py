from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"index.html",{})

from landlord.models import Landlord

def search_landlords_by_address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        landlords = Landlord.objects.filter(address__icontains=address)
        
        context = {
            'landlords': landlords,
        }
        return render(request, 'results.html', context)
    else:
        return HttpResponse("Please use the form to enter an address.")