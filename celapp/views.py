# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login ,authenticate
from django.views.generic import View
from .forms import UserForm,ProfileForm
from django.contrib import auth
from .models import Profile,team
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TeamForm
# Create your views here.
#import ipdb
@login_required
def index(request):

    # current_user = auth.get_user(request)
 #    if(current_user.username=='student'):
 #        return render(request,'celapp/student.html')
  #  if(current_user.username=='evaluator'):
   #     return render(request,'celapp/evaluator.html')
   # if(current_user.username=='expert'):
    #    return render(request,'celapp/expert.html')
    return render(request,'celapp/index.html')

@login_required
def board(request):
    team_list=team.objects.all()
    context={ 'team_list':team_list,}
    return render(request,'celapp/board.html',context)

@login_required
def tutor(request):
    return render(request,'celapp/tutor.html')


def register(request):
  #  ipdb.set_trace()
  #  ipdb.set_trace(context=5)
    if request.method == 'POST':
            user_form = UserForm(request.POST)
            profile_form = ProfileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                # usr = user_form.save(commit=False)
                # usr.save()
                
                # pro = profile_form.save(commit=False)
                # pro.user=usr
                # pro.save()

                user_form.save()
                profile_form.save(user_id=user_form.instance.id)

                messages.success(request, 'registered successfully ')
                return redirect('login')
            else:
                messages.error(request, 'wrong input given')
                return redirect('register')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'celapp/reg.html',{'user_form': user_form,'profile_form': profile_form
        })

def details(request):
    #current_user = auth.get_user(request)
    if request.method == 'POST' :
        team_form = TeamForm(request.POST)
        Student_name1=request.POST.get('student_name1')
        grade1=request.POST.get('grade1')
        age1=request.POST.get('age1')
        gender1=request.POST.get('gender1')
        expertise1=request.POST.get('expertise1')
        Student_name2=request.POST.get('student_name2')
        grade2=request.POST.get('grade2')
        age2=request.POST.get('age2')
        gender2=request.POST.get('gender2')
        expertise2=request.POST.get('expertise2')
        s=team(student_name1=Student_name1,grade1=grade1, age1=age1, gender1=gender1,expertise1=expertise1,
        student_name2=Student_name2,grade2=grade2, age2=age2, gender2=gender2,expertise2=expertise2)
        s.save()
        return redirect('teamdetails')
    else:
        team_form = TeamForm()
    return render(request, 'celapp/details.html',{'team_form': team_form})


def teamdetails(request):
    #current_user = auth.get_user(request)
    if request.method == 'POST':
        team_list=team.objects.all()
        return render(request,'celapp/teamdetails.html',{ 'team_list':team_list})
    else:
        team_list=team.objects.all()
        context={ 'team_list':team_list,}
        return render(request,'celapp/teamdetails.html',context)
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