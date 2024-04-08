from django import forms

RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

class PostReview(forms.Form):
    review = forms.CharField(max_length=255, widget=forms.Textarea)

class PostRating(forms.Form):
    rating = forms.ChoiceField(choices=RATING_CHOICES)