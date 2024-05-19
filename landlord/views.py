from django.shortcuts import render, redirect
from.forms import LandlordForm
from django.http import HttpResponse

def add_landlord(request):
    if request.method == 'POST':
        form = LandlordForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the landlord instance to the database
            return HttpResponse("Landlord information successfully saved!")
    else:
        form = LandlordForm()
    return render(request, 'add_landlord.html', {'form': form})