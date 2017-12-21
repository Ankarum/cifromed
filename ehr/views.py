from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from . import forms

def ProfileView(request):
  return render(request, 'ehr/show_profile.html')

def MainView(request):
  return render(request, 'base.html')

def EditProfileView(request):
  if request.user.is_authenticated():
    if request.method == 'POST':
      user_form = forms.UserForm(request.POST, instance=request.user)
      profile_form = forms.ProfileForm(request.POST, instance=request.user.profile)

      if all([user_form.is_valid(), profile_form.is_valid()]):
        user = user_form.save();
        profile = profile_form.save();
        return HttpResponseRedirect("../profile/")

    else:
      user_form = forms.UserForm(instance=request.user)
      profile_form = forms.ProfileForm(instance=request.user.profile)

    return render(request, 'ehr/edit_profile.html', {
      'user_form': user_form,
      'profile_form': profile_form,
      })
  else:
    return HttpResponseRedirect("/ehr/login")