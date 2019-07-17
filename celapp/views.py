# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login ,authenticate
from django.views.generic import View
from .forms import UserForm,ProfileForm
from django.contrib import auth
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    # current_user = auth.get_user(request)
 #    if(current_user.username=='student'):
 #        return render(request,'celapp/student.html')
 #    if(current_user.username=='evaluator'):
 #        return render(request,'celapp/evaluator.html')
 #    if(current_user.username=='expert'):
 #        return render(request,'celapp/expert.html')       
    return render(request,'celapp/index.html')

@login_required
def board(request):
    return render(request,'celapp/board.html')

@login_required
def details(request):
    return render(request,'celapp/details.html')

@login_required
def tutor(request):
    return render(request,'celapp/tutor.html')
    
    
    
def register(request):
    if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.schoolname = form.cleaned_data.get('schoolname')
                user.profile.contactname = form.cleaned_data.get('contactname')
                user.profile.phoneno = form.cleaned_data.get('phoneno')
                user.profile.email = form.cleaned_data.get('email')
                user_form.save()
                profile_form.save()
                raw_password = form.cleaned_data.get('password1')
                #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                user = authenticate(username=user.username, password=raw_password)
                login()
                messages.success(request, _('registered successfully '))
                return redirect('index')
            else:
                messages.error(request, _('wrong input given'))
                return redirect('register')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'celapp/reg.html',{'user_form': user_form,'profile_form': profile_form
        })  
    
    
# def register(request):
#      if request.method=='POST':
#          user.username= request.POST.get('username')
#          user.profile.contactname= request.POST.get('contactname')
#
#       
  
# def register(request):
#     if request.method == 'POST':
#             user_form = UserForm(request.POST, instance=request.user)
#             profile_form = ProfileForm(request.POST, instance=request.user.profile)
#             if form.is_valid():
#                 user = form.save()
#                 user.refresh_from_db()  # load the profile instance created by the signal
#                 user.profile.schoolname = form.cleaned_data.get('schoolname')
#                 user.profile.contactname = form.cleaned_data.get('contactname')
#                 user.profile.phoneno = form.cleaned_data.get('phoneno')
#                 user.profile.email = form.cleaned_data.get('email')
#                 user.save()
#                 raw_password = form.cleaned_data.get('password1')
#                 user = authenticate(username=user.username, password=raw_password)
#                 login(request, user)
#                 return redirect('index')
#     else:
#
#          return render(request,'celapp/reg.html')

#
# class UserFormView(View):
#     form_class=UserRegisterForm
#     template_name='celapp/reg.html'
#
#     def get(self,request):
#         form =self.form_class(None)
#         return render(request,self.template_name,{'form':form})
#
#     def post(self,request):
#            form =self.form_class(request.POST)
#
#            if form.is_valid():
#                user = form.save(commit=False)
#                username=form.cleaned_data.get('username')
#                user.refresh_from_db()  # load the profile instance created by the signal
#                user.profile.schoolname = form.cleaned_data.get('schoolname')
#                user.profile.contactname = form.cleaned_data.get('contactname')
#                user.profile.phoneno = form.cleaned_data.get('phoneno')
#                user.profile.email = form.cleaned_data.get('email')
#                user.save()
#                raw_password = form.cleaned_data.get('password1')
#                user.profile.role =orm.cleaned_data.get('role')
#                user.save()
#
#                user=authenticate(username=username,password=password)
#                if user is not None:
#                    if user.is_active:
#                        login(request,user)
#                        return redirect('index')
#            return render(request,self.template_name,{'form':form})