"""ProjectDBTM2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from divvy import views as core_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', core_views.first, name='first'),
    path('home/', core_views.home, name='home'),
    path('profile/', core_views.profile, name='profile'),
    path('editprofile/', core_views.editmember, name='edit'),
    path('notification/', core_views.notification, name='notification'),
    path('chat/', core_views.chat, name='chat'),
    path('logout/', auth_views.logout, name='logout'),
    # path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    # path('checklogin/', core_views.login, name='chklogin'),
    path('signup/', core_views.signup, name='signup'),
    path('login/',auth_views.login,name='customer_login'),
    path('promotion/<int:proid>/', core_views.showpromotion),
    path('match/<int:proid>/', core_views.match),
    path('customer/register/',core_views.CreateCustomerView.as_view(), name='customer_register'),
    # path('settings/password/', core_views.password, name='password'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
