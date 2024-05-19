# forms.py
from django import forms
from.models import Reviews

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Options for rating from 1 to 5

    class Meta:
        model = Reviews
        fields = ['tenant', 'rating', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget = forms.Select(choices=self.RATING_CHOICES)
