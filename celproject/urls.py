"""celproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from celapp import views
urlpatterns = [
    url('',include('celapp.urls')),
    url(r'^admin/', admin.site.urls),
    url('login/',auth_views.LoginView.as_view(template_name='celapp/login.html'),name='login'),
       url('logout/',auth_views.LogoutView.as_view(template_name='celapp/logout.html'),name='logout'),
      # url(r'^reg/', views.UserFormView.as_view(), name='reg'),
       url(r'^register/', views.register, name='register'),
]
