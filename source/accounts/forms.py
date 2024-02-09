from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'avatar', 'gender',
            'phone_number',
            'user_information')


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'avatar', 'gender', 'phone_number', 'user_information')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Поиск')