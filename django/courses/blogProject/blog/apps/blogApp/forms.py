from django import forms
from .models import BlogCategory

class BlogPostForm(forms.Form):
    title=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    category=forms.ModelMultipleChoiceField(queryset=BlogCategory.objects.all(),
                                             widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

    