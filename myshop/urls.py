from django.urls import path
from myshop import views
app_name = 'myshop'
urlpatterns = [
    path('<str:code>/',views.ShopCatalogueView.as_view(),name='myshop-view'),
]