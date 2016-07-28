from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.view_categories, name='view_categories'),
    url(r'^view_category/(?P<id>\d+)/$', views.view_category, name='view_category'),
    url(r'^view_products/$', views.view_products, name='view_products'),
    url(r'^view_orders/$', views.view_orders, name='view_orders'),
]