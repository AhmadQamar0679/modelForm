from django.urls import path
from . import views




urlpatterns = [
    
    path('',views.home_modelForm,name='home_modelForm')
]
