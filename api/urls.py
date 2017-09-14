from django.conf.urls import url
from . import views

urlpatterns = [
    # API анкет клиентов
    url(r'^customerProfile/$', views.CustomerProfileList.as_view()),
    url(r'^customerProfile/(?P<pk>[0-9]+)/$', views.CustomerProfileDetail.as_view()),
    # API заявок в кредитные организации
    url(r'^request2CreditOrganization/$', views.Request2coList.as_view()),
    url(r'^request2CreditOrganization/(?P<pk>[0-9]+)/$', views.Request2coDetail.as_view()),
]