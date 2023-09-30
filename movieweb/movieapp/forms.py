from django import forms

from movieapp.models import movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = movie
        fields = ['mname','year','img','desc']

