from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    author = forms.CharField(label='Author', max_length=100)
    # identifier = forms.CharField(label='Identifier(ISBN, Google-id, amazon id)', max_length=20)

