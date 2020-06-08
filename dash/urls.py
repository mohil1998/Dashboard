from django.contrib import admin
from django.urls import path,include
from . import views
app_name='dash'
urlpatterns = [
    path('',views.connectdash,name="connectdash"),
    path('createDash',views.createdash,name="createdash"),
    path('viewDash',views.viewdash,name="viewdash"),
]
