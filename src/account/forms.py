from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account
from blog.models import BlogPost

class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=60, help_text="Hello, try again!")
    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

class AuthenticateForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ("email", "password")
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Something wrong email or password")

class AccountUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" already exists.' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" already exists.' % username)

