from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view),
    path('submit/', views.submit_form, name='submit_form'),
    path('thankyou/', views.thank_you, name='thank_you'),
]