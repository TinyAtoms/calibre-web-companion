from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class SearchForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    author = forms.CharField(label='Author', max_length=100)
    identifier = forms.CharField(label='Identifier(ISBN, Google-id, amazon id)', max_length=20)
    generic = forms.CharField(label='All', max_length=100, required=False)



class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
