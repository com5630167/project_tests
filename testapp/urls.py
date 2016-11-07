from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from testapp import views


urlpatterns = [
    url(r'^$',views.home_page, name='home'),
    url(r'^vis',views.vis_page, name="vis"),
    url(r'^openL',views.openL_page, name="openL"),
    url(r'^leaft',views.leaft_page, name="leaft"),
    url(r'^arc',views.arc_page, name="arc"),
    #url(r'^$',data, name='data'),
    #url(r'calculate/$','SaveMoney.views.result_page',name='calculate'),
    #url(r'^$',charts.simple), #---page fig
]

                       
                   
