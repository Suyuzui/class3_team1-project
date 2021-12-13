from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    context = forms.CharField(label='内容'、widget=forms.Textarea())