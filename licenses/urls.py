from django.urls import path


from . import views

urlpatterns = [
    path('d/<int:NID>', views.getDriver),
    path('c/<int:tarmeez>/<int:carNo>/<int:regNo>', views.getCar)
]