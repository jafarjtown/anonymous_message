from django.urls import path

from .views import Index, clear, create, sendMessage, view
app_name = 'message'
urlpatterns = [
    path("", Index, name="home"),
    path("cr/", create, name="home"),
    path("clear/", clear, name="home"),
    path("vr/<str:link>", view, name="home"),
    path("sn/<str:link>", sendMessage, name="home"),
]
