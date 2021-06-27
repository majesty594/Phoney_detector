from django import forms

class get_data(forms.Form):
    search = forms.URLField(widget=forms.URLInput(attrs={'class':'form-control','placeholder':'Enter the news here'}))