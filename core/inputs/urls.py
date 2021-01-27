from django.urls import path
from . import views


urlpatterns = [
    path('', views.inputs, name='inputs'),
    path('add_input', views.add, name='add'),
    path('send', views.send, name='send'),
]