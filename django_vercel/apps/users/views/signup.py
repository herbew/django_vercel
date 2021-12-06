# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from allauth.utils import get_form_class
from allauth.account import app_settings


from django_vercel.apps.users.models.users import User

from django_vercel.apps.accounts.forms import SignupForm


class SignupView(SignupView):
    """ SignUp as admin33
    """
    form_class = SignupForm
    
    def get_form_class(self):
        return get_form_class(app_settings.FORMS, 'signup', self.form_class)
    
    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)

        return context
    
    def get_success_url(self):
        return reverse_lazy('users:redirect')
    
    def form_valid(self, form):
        user = form.save(self.request)
        user.is_active = False
        user.save()
        messages.success(
        self.request, _("Registration account %s have successfully. Please contact to Admin for activating account.") % str(user.username))
        
        return complete_signup(self.request, user,
                               app_settings.EMAIL_VERIFICATION,
                               self.get_success_url())
        

signup = SignupView.as_view()


