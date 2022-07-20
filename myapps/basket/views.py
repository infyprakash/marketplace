# from oscar.apps.basket.views import BasketAddView as BasketAddViewCore 
# from django import shortcuts
# from django.contrib import messages
# from django.contrib.sessions.serializers import JSONSerializer
# from django.core.exceptions import ObjectDoesNotExist
# from django.http import JsonResponse, QueryDict
# from django.shortcuts import redirect
# from django.template.loader import render_to_string
# from django.urls import reverse
# from django.utils.http import url_has_allowed_host_and_scheme
# from django.utils.translation import gettext_lazy as _
# from django.views.generic import FormView, View
# from extra_views import ModelFormSetView

# from oscar.apps.basket.signals import (basket_addition, voucher_addition, voucher_removal)
# # from oscar.core import ajax
# from oscar.core.loading import get_class, get_classes, get_model
# # from oscar.core.utils import is_ajax, redirect_to_referrer, safe_referrer

# Applicator = get_class('offer.applicator', 'Applicator')
# (BasketLineForm, AddToBasketForm, BasketVoucherForm, SavedLineForm) = get_classes(
#     'basket.forms', ('BasketLineForm', 'AddToBasketForm',
#                      'BasketVoucherForm', 'SavedLineForm'))
# BasketLineFormSet, SavedLineFormSet = get_classes(
#     'basket.formsets', ('BasketLineFormSet', 'SavedLineFormSet'))
# Repository = get_class('shipping.repository', 'Repository')

# OrderTotalCalculator = get_class(
#     'checkout.calculators', 'OrderTotalCalculator')
# BasketMessageGenerator = get_class('basket.utils', 'BasketMessageGenerator')
# SurchargeApplicator = get_class("checkout.applicator", "SurchargeApplicator")


# class BasketAddView(BasketAddViewCore):
#     def form_valid(self, form):
#         print(self.request.basket.lines)
#         print(form.cleaned_options())
#         print(self.request.POST)
#         print(form.product)
#         options = form.cleaned_options()
#         for data in self.request.POST:
#             if(data!='quantity' and data!='csrfmiddlewaretoken'):
#                 print(data)
#                 options.append({"option": str(data), "value": self.request.POST[data]})
#                 print(data,self.request.POST[str(data)])
#         print(options)
#         self.request.basket.add_product(
#             form.product, form.cleaned_data['quantity'],
#             options)
#         return super().form_valid(form)



