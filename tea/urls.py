from django.conf.urls import url

from tea.views import *

urlpatterns = [
    url(r'^$', ProductsList.as_view(), name='products_list'),
    url(r'^page/(?P<page>\d+)/$', ProductsList.as_view(), name='products_list'),
    url(r'^add_product/$', ProductCreate.as_view(), name='add_product'),
    url(r'^product/(?P<id>\d+)/$', ProductDetail.as_view(), name='product_detail'),
    url(r'^product/(?P<id>\d+)/delete/$', ProductDelete.as_view(), name='product_delete'),
    url(r'^product/(?P<id>\d+)/update/$', ProductUpdate.as_view(), name='product_update'),
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^add_buyer/$', BuyerCreate.as_view(), name='add_buyer'),
]