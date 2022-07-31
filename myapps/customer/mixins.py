from oscar.apps.customer.mixins import RegisterUserMixin as RegisterUserMixinCore
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
# from .forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  

from django.contrib.auth import login as auth_login

class RegisterUserMixin(RegisterUserMixinCore):
    def register_user(self, form):
        """
        Create a user instance and send a new registration email (if configured
        to).
        """
        user = form.save(commit=False)
        user.is_active = False  
        user.save()

        current_site = get_current_site(self.request)  
        mail_subject = 'Activation link has been sent to your email id'  
        message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': self.request.get_host(),  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),
                })
        to_email = form.cleaned_data.get('email')  
        email = EmailMessage(  
                        mail_subject, message, to=[to_email]
                        )
        email.send() 
        # Raise signal robustly (we don't want exceptions to crash the request
        # handling).
        # user_registered.send_robust(
        #     sender=self, request=self.request, user=user)

        # if getattr(settings, 'OSCAR_SEND_REGISTRATION_EMAIL', True):
        #     self.send_registration_email(user)

        # We have to authenticate before login
        try:
            user = authenticate(
                username=user.email,
                password=form.cleaned_data['password1'])
        except User.MultipleObjectsReturned:
            # Handle race condition where the registration request is made
            # multiple times in quick succession.  This leads to both requests
            # passing the uniqueness check and creating users (as the first one
            # hasn't committed when the second one runs the check).  We retain
            # the first one and deactivate the dupes.
            logger.warning(
                'Multiple users with identical email address and password'
                'were found. Marking all but one as not active.')
            # As this section explicitly deals with the form being submitted
            # twice, this is about the only place in Oscar where we don't
            # ignore capitalisation when looking up an email address.
            # We might otherwise accidentally mark unrelated users as inactive
            users = User.objects.filter(email=user.email)
            user = users[0]
            for u in users[1:]:
                u.is_active = False
                u.save()

        # auth_login(self.request, user)

        return user