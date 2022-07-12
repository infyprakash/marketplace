from django.urls import path
from myshop import views
app_name = 'myshop'
urlpatterns = [
    path('<str:code>/',views.ShopCatalogueView.as_view(),name='myshop-view'),
    path('<str:code>/add/fb/messanger',views.FbChatAddView.as_view(),name="addfbchat-view"),
    path('<str:code>/update/fb/messanger',views.FbChatUpdateView.as_view(),name="addfbchat-view"),
]