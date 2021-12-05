from __future__ import unicode_literals, absolute_import

import logging

from collections import OrderedDict

from django import forms
from django.utils.safestring import mark_safe
from django.forms.widgets import Select, TextInput, CheckboxInput
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _

from django_vercel.apps.users.models.users import User


log = logging.getLogger(__name__)

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('name','gender',
#                   'birth_city', 'birth_date',
#                   'address', 'mobile'
                  )

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        
        
        
        self.fields['name'].required=True
        self.fields['name'].label = _("Name")
        self.fields['name'].label =  mark_safe("%s <font color=red size=4.5em>*</font>" % self.fields['name'].label)
        
        self.fields['gender'].choices=tuple([('', _('Select Gender ---'))] + \
                                list(User.GENDER_CHOICES))
        self.fields['gender'].required=True
        self.fields['gender'].label =  mark_safe("%s <font color=red size=4.5em>*</font>" % self.fields['gender'].label)
        
    



