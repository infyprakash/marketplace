from email.mime import message
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render,redirect
from dashboard.partners.views import PartnerAddress
from oscar.apps.partner.models import Partner,StockRecord
from myshop.models import FbChatModel
# Create your views here.

class ShopCatalogueView(View):
    def get(self,request,code):
        partner = Partner.objects.get(code=code)
        stocks = StockRecord.objects.filter(partner__id=partner.id)
        address = PartnerAddress.objects.get(partner__id=partner.id)
        f = FbChatModel.objects.get(partner__code=partner.code)
        return render(request,'oscar/myshop/shop_catalogue.html',{'stocks':stocks,'address':address,'partner':partner,'code':f.code})

class FbChatAddView(View):
    def get(self,request,code):
        if request.user.is_authenticated:
            partner = Partner.objects.get(code=code)
            return render(request,'oscar/myshop/add_fb_chat.html',{'partner':partner})
        else:
            return redirect('/accounts/login/')
    def post(self,request,code):
        if request.user.is_authenticated:
            partner = Partner.objects.get(code=code)
            plugin_code = request.POST['code']
            chat = FbChatModel.objects.create(partner=partner,code=plugin_code)
            if chat is not None:
                return redirect('/at/{}'.format(code))
            else:
                return redirect('/at/{}/add/fb/messanger'.format(code))
        else:
            return redirect('/accounts/login/')




