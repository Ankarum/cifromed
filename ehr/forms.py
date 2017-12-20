from django import forms

from django.contrib.auth.models import User

from .models import Profile

from crispy_forms.helper import FormHelper

from django.utils.translation import gettext_lazy as _

from django.contrib.admin.widgets import AdminDateWidget 

from bootstrap_datepicker.widgets import DatePicker

class UserForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(UserForm, self).__init__(*args, **kwargs)

    self.helper = FormHelper(self)
    self.helper.form_tag = False

    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-lg-2'
    self.helper.field_class = 'col-lg-8'

  class Meta:
    model = User
    fields = ( 'email', 'first_name', 'last_name')
    labels = {
        'email' : _('email'),
        'first_name' : _('Имя'),
        'last_name' : _('Фамилия'),
    }

class ProfileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)

    self.helper = FormHelper(self)
    self.helper.form_tag = False

    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-lg-2'
    self.helper.field_class = 'col-lg-8'

  class Meta:
    model = Profile
    fields = ('middle_name', 'birthday', 'sex', 'city', 'postcode', 'region', 'street',
    'housing', 'structure', 'house', 'apartment', 'mobile_phone', 'company', 'profession',
    'position', 'insurance_policy', 'SNILS', 'passport')

    widgets = {
        'birthday' : forms.DateInput(attrs={'class':'datepicker'}),
    }




