from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:pk>/apply/', views.apply_company, name='apply_company'),
    path('applications/', views.application_list, name='application_list'),
    path('off-campus/', views.off_campus_list, name='off_campus_list'),
    path('off-campus/add/', views.add_off_campus, name='add_off_campus'),
    path('policy/', views.policy_page, name='policy'),
]