from django import urls
from django.urls import path
from . import views
urlpatterns = [
   path('1', views.req1F),
   path('2', views.req2F),
   path('3', views.req3F),
   path('4', views.req4F), #NID,tarmeez, Num, regNo, deli, addr
   path('5', views.req5F), #NID,tarmeez, Num, regNo, deli, addr
   path('6', views.req6F), #NID,tarmeez, Num, regNo, deli, addr
   path('7', views.req7F), #NID,tarmeez, Num, regNo, deli, addr
   path('11', views.req11F), #NID,tarmeez, Num, regNo, deli, addr
   path('getAll/<int:NID>', views.getAll),
   path('payAll', views.payAll),
   path('payone', views.payone),


]