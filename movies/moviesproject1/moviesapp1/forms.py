from django import forms
from . models import movies_dtl

class MovieForm(forms.ModelForm):
    class Meta:
        model=movies_dtl
        fields=['name','year','desc','pic']

