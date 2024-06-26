# diary_app/forms.py

# diary_app/forms.py
##################################################

# diary_app/forms.py


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Entry


User = get_user_model()
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text', 'published_date', 'image', 'people_links']
        widgets = {
            'published_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        # Исключаем поле author из формы, чтобы его значение не редактировалось
        exclude = ['author']
#class EntryForm(forms.ModelForm):
#    class Meta:
#        model = Entry
#        fields = ['title', 'text', 'published_date', 'author', 'image', 'people_links']#

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")#######