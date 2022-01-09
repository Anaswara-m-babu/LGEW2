from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('adminhome', views.adminhome),
    path('addbustime', views.AddBusTime),
    path('busmanagement', views.busmanagement),
    path('addconductor', views.addconductor),
    path('busmanagement_add', views.busmanagement_add),
    path('bustime', views.bustime),
    path('addstop', views.AddStop),
    path('conductor', views.conductor,name="Conductor"),
    path('feedback', views.feedback),
    path('login', views.login1),
    path('passenger', views.passenger),
    path('route', views.Route),
    path('routeadd', views.RouteAdd),
    path('stopdetails', views.stopdetails),
    path('track', views.track),
]
