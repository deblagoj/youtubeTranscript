from django import forms

class InsertYoutubeLink(forms.Form):
    youtube_URL = forms.CharField(label='valid youtube url', max_length=100)

