from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm 
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserForm,MemberForm
from .models import Member,Promotion , Interest
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.views import logout


from social_django.models import UserSocialAuth


class CreateCustomerView(CreateView):
	queryset = User()
	template_name='register.html'
	form_class = UserForm
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
    status = False
    interest = Interest.objects.filter(mid = request.user.member.mid)
    for i in interest:
        if i.matching and not i.status:
            status = True
            break
    promotions = Promotion.objects.all()
    interest = Interest
    return render(request, './home.html',{'promotions' : promotions , 'status' : status })

@login_required
def profile(request):
    status = False
    interest = Interest.objects.filter(mid = request.user.member.mid)
    for i in interest:
        if i.matching and not i.status:
            status = True
            break
            
    member = Member.objects.get(user=request.user)
    return render(request, './profile.html', {'member' : member , 'status' : status } )

def first(request):
    return render(request, './selectlogin.html')

@login_required
def showpromotion(request,proid):
    status = False
    interest = Interest.objects.filter(mid = request.user.member.mid)
    for i in interest:
        if i.matching and i.status:
            status = True
            break
    promotion = Promotion.objects.get(pid = proid)
    try:
        interest = Interest.objects.get(mid = request.user.member.mid, pid = proid)
    except Interest.DoesNotExist:
        interest = None
    print(status,interest)
    return render(request, './match.html',{'promotion':promotion ,'interest': interest, 'status' : status })

@login_required
def logout(request):
     logout(request)
     return redirect('login')   
        
@login_required
def editmember(request):
    status = False
    interest = Interest.objects.filter(mid = request.user.member.mid)
    for i in interest:
        if i.matching and not i.status:
            status = True
            break
    formset = MemberForm()
    if request.method == 'POST':
        formset = MemberForm(request.POST, request.FILES)
        if formset.is_valid():
            member = Member.objects.get(user=request.user)
            member.user = request.user
            member.name =  formset.cleaned_data["name"]
            member.image = formset.cleaned_data["image"]
            member.phone = formset.cleaned_data["phone"]
            member.save()
            return redirect('/profile')   
        
    return render(request, 'editmember.html', {'formset': formset,'status':status})

@login_required
def match(request,proid):

    promotion = Promotion.objects.get(pid = proid)
    user = Member.objects.get(user =request.user)
    try:
        interest = Interest.objects.filter(pid = promotion,matching=None).first()
    except Interest.DoesNotExist:
        interest = None
   
    if(interest):
        interest.matching = user
        interest.save()
        interest2 = Interest.objects.create(pid = promotion, mid = user,matching = interest.mid)        
    else:
        interest2 = Interest.objects.create(pid = promotion, mid = user)
        
    return redirect('/home')   

@login_required
def notification(request):
    interest = Interest.objects.filter(mid = request.user.member.mid)
    for i in interest:
        if i.matching:
            i.status = True
            i.save()

    return render(request, 'notification.html', {'interest': interest })

@login_required
def chat(request):

    return render(request, 'chat.html')

