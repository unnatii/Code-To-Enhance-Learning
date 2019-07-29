# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, blank=True)
    schoolname = models.CharField(max_length=30, blank=True)
    contactname=models.CharField(max_length=20, blank=True)
    phoneno = models.CharField(max_length=10, blank=True)
    #objects = models.Manager()

    def __str__(self):
        return u"{} | {} | {} |  {} | {} ".format(self.user,self.role,self.schoolname,self.contactname,self.phoneno)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

class team(models.Model):
    student_name1= models.CharField(max_length=50)
    grade1=models.IntegerField(default=0)
    age1=models.IntegerField(default=0)
    gender1=models.CharField(max_length=20)
    expertise1=models.CharField(max_length=20)
    student_name2= models.CharField(max_length=50)
    grade2=models.IntegerField(default=0)
    age2=models.IntegerField(default=0)
    gender2=models.CharField(max_length=20)
    expertise2=models.CharField(max_length=20)



    def __str__(self):
        return u"{} | {} | {} |  {} | {} | {} | {} | {} |  {} | {}".format(self.student_name1,self.grade1,self.age1,self.gender1,self.expertise1,self.student_name2,self.grade2,self.age2,self.gender2,self.expertise2)

    def get_absolute_url(self):
        return reverse('index')
