from django import forms
from .views import *

class add_listing(forms.Form):
    head =forms.CharField(label="title")
    body=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),label="describtion")
    file = forms.FileField()
    #bid=forms.FloatField()
"""
def handle_uploaded_file(f):
    with open(f'auctions/pic/{head}.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
"""
class Bidform(forms.Form):

    bid=forms.FloatField(max_value=5000)
