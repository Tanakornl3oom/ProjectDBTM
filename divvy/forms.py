
from .models import Customer
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit , Field


class CustomerForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
    
	class Meta:
		model =  Customer
		exclude=['cid']
		fields = ['username','password','email','image']


		
	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		# self.helper.layout = Layout(
        #     Field('username'),
        #     Field('password', css_class="passwordfields")
        # )
		self.helper.add_input(Submit('submit', 'Register'))
		