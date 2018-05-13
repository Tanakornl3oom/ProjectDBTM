
from .models import Member
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit , Field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    username = forms.CharField( help_text='Letters, digits and @/./+/-/_ only.')
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput , help_text='Your Password Must Have at least 8 characters and not Numeric Only')
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)
    email = forms.EmailField(max_length=254, help_text='Required valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
    def __init__(self, *args, **kwargs):
	    super(UserForm, self).__init__(*args, **kwargs)
	    self.helper = FormHelper()
	    self.helper.add_input(Submit('submit', 'Register'))
    
    # def save(self, *args, **kwargs):
    #     super(UserForm, self).save(*args, **kwargs)
    #     //create model member


class MemberForm(ModelForm):
        
    class Meta:
        model = Member
        fields = ['name','phone','image']