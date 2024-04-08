from django import forms




class SignUpForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=255)
    password=forms.CharField(max_length=255,widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=255,widget=forms.PasswordInput)



class LoginForm(forms.Form):
    email=forms.EmailField(max_length=255)
    password=forms.CharField(max_length=255,widget=forms.PasswordInput)