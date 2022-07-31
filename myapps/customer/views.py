from oscar.core.compat import get_user_model
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from .tokens import account_activation_token  
from oscar.apps.customer.views import AccountRegistrationView as AccountRegistrationViewCore,AccountAuthView as AccountAuthViewCore
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

class AccountAuthView(AccountAuthViewCore):
    def get_registration_success_message(self, form):
        return _("Thanks for registering! Activation link has been sent to your email id| Please confirm your email address to complete the registration")

class AccountRegistrationView(AccountRegistrationViewCore):
    def form_valid(self, form):
        self.register_user(form)
        return HttpResponse('Please confirm your email address to complete the registration')

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account. <a href="/accounts/login/">Login</a>')  
    else:  
        return HttpResponse('Activation link is invalid!')  