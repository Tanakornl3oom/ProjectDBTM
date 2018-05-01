from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
# from django.contrib.auth.models import customer




from social_django.models import UserSocialAuth


class CreateCustomerView(CreateView):
	queryset = Customer()
	template_name='register.html'
	form_class = CustomerForm
	success_url = '/login/'

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(CreateCustomerView, self).form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, './signup.html', {'form': form})

@login_required
def home(request):
    return render(request, './home.html')


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, './password.html', {'form': form})

@login_required
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        Customer = authenticate(request, username=username, password=password)
        if Customer is not None:
            print("user login suss")
            login(request, Customer)
            messages.success(request, 'login Susscess')
            return redirect('/')            
        else:
            print("user login failed")            
            messages.error(request, 'Username or password invalid')
    else:
        messages.error(request, 'Error method')
    return redirect('/customer/login/')            
        
        