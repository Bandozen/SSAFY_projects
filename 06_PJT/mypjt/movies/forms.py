from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description')

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = '리뷰',
        widget = forms.TextInput(
            attrs={
                'placeholder': '리뷰를 남겨주세요.'
            }
        ),
    )
    class Meta:
        model = Comment
        exclude = ('movie', 'user')