from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)



User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs = {"placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {"placeholder": "password"}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Icorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user does not active')

            return super(UserLoginForm, self).clean(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs = {"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs = {"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {"placeholder": "password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = {"placeholder": "repeat password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean(self,*args,**kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        email = self.cleaned_data.get('email')

        if password != password2:
            raise forms.ValidationError("passwords must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This Email is already exists")
        return super(RegisterForm,self).clean(*args,**kwargs)