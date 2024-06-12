from django.urls import path,include

from .views import *

app_name = 'account'

urlpatterns = [
    path('dashboard/appointments/', ApointmentListView.as_view(), name='apointment'),
    path('appointments/delete/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment-delete'),

    path("", include('django.contrib.auth.urls')),
    path("signup/", SignUpView.as_view(),name="signup"),
    path("dashboard/", AdminView.as_view(),name="admin"),
    path("dashboard/lawyers/", LawyerListView.as_view(),name="lawyer-list"),
    path("dashboard/lawyers/<str:slug>/", LawyerDetailView.as_view(),name="lawyer-details"),
    path("dashboard/edit/", UserEditCreateView.as_view(),name="edit"),

    
]

 
   