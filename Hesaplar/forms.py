from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class loginForm(forms.Form):
    username =  forms.CharField(max_length=100 ,label='Kullanıcı Adı')
    password = forms.CharField(max_length=100 ,label="Parola",widget=forms.PasswordInput)

    def clean(self):
        kullanici = self.cleaned_data.get('username')
        parola = self.cleaned_data.get('password')
        if kullanici and parola:
            dogru = authenticate(username=kullanici,password=parola)
            if dogru is None:
                raise forms.ValidationError('kullanici Adi veya parola yanliştir')
        return super(loginForm,self).clean()


class registerForm(forms.ModelForm):
    username =  forms.CharField(max_length=100 ,label='Kullanıcı Adı')
    password1 = forms.CharField(max_length=100 ,label="Parola",widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100 ,label="Parola Doğrulama",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('parolalar eşleşmiyor')
        return password2
