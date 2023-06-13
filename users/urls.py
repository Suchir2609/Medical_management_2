from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('staff_login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='staff-login'),
    path('staff_home/', views.AppointmentListView.as_view(), name='staff-home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('patient_home/', views.AppointmentListViewPatient.as_view(), name='patient-home'),
    path('patient_home/new_appointment', views.AppointmentCreateView.as_view(), name='new-appointment'),
    path('appointment/<int:pk>/update/', views.appointment_update, name='appointment-update'),
    path('doctor_create/', views.doctor_create, name='doctor-create'),
    path('doctor_update/<int:pk>', views.doctor_update, name='doctor-update'),
    path('appointment_status/<int:pk>', views.appointment_status, name='appointment-status'),
    ]
