from django import urls
from django.urls import path
from . import views
urlpatterns = [
   path('1', views.req1F),
   path('2/<int:NID>/<int:lno>/<int:deli>/<slug:addr>', views.req2F),
   path('3/<int:NID>/<int:lno>/<int:deli>/<slug:addr>', views.req3F),
   path('4/<int:NID>/<int:lno>/<int:deli>/<slug:addr>', views.req4F), #NID,tarmeez, Num, regNo, deli, addr
   path('5/<int:NID>/<int:tarmeez>/<int:Num>/<int:regNo>/<int:deli>/<slug:addr>', views.req5F), #NID,tarmeez, Num, regNo, deli, addr
   path('6/<int:NID>/<int:tarmeez>/<int:Num>/<int:regNo>/<int:deli>/<slug:addr>', views.req6F), #NID,tarmeez, Num, regNo, deli, addr
   path('7/<int:NID>/<int:tarmeez>/<int:Num>/<int:regNo>/<int:deli>/<slug:addr>', views.req7F), #NID,tarmeez, Num, regNo, deli, addr
   path('11/<int:NID>/<int:NID2>/<slug:phone>/<int:tarmeez>/<int:Num>/<int:regNo>', views.req11F), #NID,tarmeez, Num, regNo, deli, addr
   path('getAll/<int:NID>', views.getAll),
   path('payAll/<int:NID>', views.payAll),
   path('payone/<slug:ID>', views.payone),


]