from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 

class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #widget is a html form element
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}), required=False)
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
        }
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        
        if commit:
            user.save()
        return user
