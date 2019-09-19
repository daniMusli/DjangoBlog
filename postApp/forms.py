from django import forms
from .models import post,comment
from captcha.fields import ReCaptchaField

class postForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model=post
        fields = [
            'title',
            'content',
            'image',
        ]

class commentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model=comment
        fields = ['name','content',]


