from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from . import forms

# Create your views here.
class RegisterFormView(FormView):
	form_class = UserCreationForm

	success_url = "/ehr/login/"

	template_name = "ehr/register.html"

	def form_valid(self, form):
		form.save()

		return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
	form_class = AuthenticationForm

	template_name = "ehr/login.html"

	success_url = "/ehr/profile/"

	def form_valid(self, form):
		self.user = form.get_user()

		login(self.request, self.user)
		return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect("/ehr/login")

def ProfileView(request):
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

    return render(request, 'ehr/profile.html', {
      'user_form': user_form,
      'profile_form': profile_form,
      })
  else:
    return HttpResponseRedirect("/ehr/login")