from django.urls import path
from . import views




urlpatterns = [
    
    path('',views.home_modelForm,name='home_modelForm'),
    path('studentlist/',views.student_list,name="student_list"),
    path('<detail:id>/',views.student_detail , name='student_detail')
]
