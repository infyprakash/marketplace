from django.http import HttpResponse
from django.views import View
from django.shortcuts import render,redirect
from oscar.apps.dashboard.partners.forms import PartnerCreateForm
from oscar.apps.partner.models import Partner
from oscar.apps.address.models import Country
from dashboard.partners.forms import  PartnerAddressForm
from django.contrib.auth.models import Permission

from oscar.core.loading import get_class, get_model
PartnerAddress = get_model('partner', 'PartnerAddress')




# view starts here 
class PartnerManageView(View):
    def get(self,request):
        if request.user.is_authenticated:
            shops = Partner.objects.filter(users__id =request.user.id)
            return render(request,'oscar/dashboard/partners/manage_shops.html',{'shops':shops})
        else:
            return redirect('/accounts/login/')

class PartnerUpdateView(View):
    def get(self,request,code):
        if request.user.is_authenticated:
            partner = Partner.objects.get(code=code)
            partner_address = PartnerAddress.objects.get(partner__id=partner.id)
            form = PartnerAddressForm(instance=partner_address)
            return render(request,'oscar/dashboard/partners/update_shops.html',{'shop_update_form':form})
        else:
            return redirect('/accounts/login/')
    def post(self,request,code):
        if request.user.is_authenticated:
            # u = Partner.objects.filter(users__id =request.user.id)
            name = request.POST['name']
            line1 = request.POST['line1']
            country = request.POST['country']
            partner = Partner.objects.get(code=code)
            partner_address = PartnerAddress.objects.get(partner__id=partner.id)
            if name is not None:
                partner.name = name 
                partner.save()
            if line1 is not None:
                partner_address.line1 = line1 
                c = Country.objects.get(name=country)
                partner_address.country = c 
                partner_address.save()
            return redirect('/dashboard/partner/manage/shop/')
        else:
            return redirect('/accounts/login/')
    

class PartnerRegisterView(View):
    def get(self,request):
        if request.user.is_authenticated:
            form = PartnerAddressForm()
            return render(request,'oscar/dashboard/partners/partner_register.html',{'partner_register_form':form})
        else:
            return redirect('/accounts/login/')
    def post(self,request):
        if request.user.is_authenticated:
            print("testing...................")
            # u = Partner.objects.filter(users__id =request.user.id)
            name = request.POST['name']
            line1 = request.POST['line1']
            country = request.POST['country']
            # print(name,line1,country)
            partner = Partner.objects.create(name=request.POST['name'])
            user = request.user
            partner.users.add(user)
            c = Country.objects.get(name=country)
            p_addr = PartnerAddress.objects.create(partner=partner,line1=line1,country=c)
            if not user.is_staff:
                dashboard_access_perm = Permission.objects.get(codename='dashboard_access',content_type__app_label='partner')
                user.user_permissions.add(dashboard_access_perm)
                return redirect('/dashboard')
        else:
            return redirect('/accounts/login/')

