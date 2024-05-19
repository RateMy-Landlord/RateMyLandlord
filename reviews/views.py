from django.shortcuts import render, get_object_or_404
from .models import Reviews
from.forms import ReviewForm
from landlord.models import Landlord
from django.http import HttpResponse
from django.db.models import Avg

def landlord_detail(request, landlord_id):
    landlord = get_object_or_404(Landlord, pk=landlord_id)
    reviews = Reviews.objects.filter(lord=landlord)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'landlord_detail.html', {'landlord': landlord, 'reviews': reviews, 'average': avg_rating})

def add_review(request, landlord_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.lord = Landlord.objects.get(pk=landlord_id)
            review.save()
            return HttpResponse("Review successfully saved!")
        else:
            return HttpResponse("Review upload failed!")
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})
