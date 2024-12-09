from django import forms

class QuizForm(forms.Form):
    answers = forms.CharField(widget=forms.Textarea)