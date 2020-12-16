from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contacts', views.contacts, name='contacts'),
    path('logs', views.logs, name='logs'),
    path('addlog', views.addlog, name='addlog'),
    path('addcontact', views.addcontact, name='addcontact'),
    path('add', views.add, name='add'),
    path('search', views.search, name='search'),
    path('deletelog', views.delete, name='delete'),
]