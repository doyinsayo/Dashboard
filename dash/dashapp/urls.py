from django.urls import path
from . import views

app_name = 'dashapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('send_email',views.send_email,name='send_email')
]