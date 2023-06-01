from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    score = forms.FloatField(

        widget=forms.NumberInput(
        attrs={
        'type' : 'range',
        'min' : '0',
        'max' : '5',
        'step' : '0.5',
        }
        )
    )

    release_Date = forms.DateField(

        widget=forms.DateInput(
        attrs={
        'type' : 'date'
        }
        )
    )


    class Meta:
        model = Movie
        fields = '__all__'