from oscar.apps.dashboard.partners.forms  import  PartnerAddressForm as  PartnerAddressFormCore
from oscar.core.loading import get_class, get_model
from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy
# User = get_user_model()
# Partner = get_model('partner', 'Partner')
PartnerAddress = get_model('partner', 'PartnerAddress')


class PartnerAddressForm(PartnerAddressFormCore):
    name = forms.CharField(
        required=False, max_length=128,
        label=pgettext_lazy("Partner's name", "Name"))

    class Meta:
        fields = ('name', 'line1', 'country')
        model = PartnerAddress