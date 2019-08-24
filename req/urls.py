from django import urls
from django.urls import path
from . import views
urlpatterns = [
   path('1/<int:NID>/<int:NID2>/<int:ltype>', views.req1F)
    
]