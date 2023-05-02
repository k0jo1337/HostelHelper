from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from account.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'surname', 'room_number', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = None
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = None
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = None
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['surname'].widget.attrs['class'] = 'form-control'
        self.fields['room_number'].widget.attrs['class'] = 'form-control'


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

"""
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'surname', 'room_number', 'email', 'password1', 'password2')"""