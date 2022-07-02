from django.urls import path
from .partners import views
app_name = 'dashboard.partner'
urlpatterns = [
    path('register/shop/',views.PartnerRegisterView.as_view(),name='partner-register'),
    path('manage/shop/',views.PartnerManageView.as_view(),name='partner-manage'),
    path('update/shop/<str:code>',views.PartnerUpdateView.as_view(),name='partner-update'),
]
