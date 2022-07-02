from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render,redirect
from dashboard.partners.views import PartnerAddress
from oscar.apps.partner.models import Partner,StockRecord
# Create your views here.

class ShopCatalogueView(View):
    def get(self,request,code):
        partner = Partner.objects.get(code=code)
        stocks = StockRecord.objects.filter(partner__id=partner.id)
        address = PartnerAddress.objects.get(partner__id=partner.id)
        return render(request,'oscar/myshop/shop_catalogue.html',{'stocks':stocks,'address':address,'partner':partner})



