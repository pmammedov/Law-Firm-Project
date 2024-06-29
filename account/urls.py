from django.urls import path,include

from .views import *

app_name = 'account'

urlpatterns = [
    path('dashboard/appointments/', ApointmentListView.as_view(), name='apointment'),
    path('appointments/delete/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment-delete'),

    path("", include('django.contrib.auth.urls')),
    path("signup/", SignUpView.as_view(),name="signup"),
    path("dashboard/", AdminView.as_view(),name="admin"),
    path('dashboard/lawyers/create/', CreateLawyerView.as_view(), name='create_lawyer'),
    path('dashboard/lawyers/<int:pk>/', LawyerDetailView.as_view(), name='lawyer-details'),
    path('dashboard/lawyers/', LawyerListView.as_view(), name='lawyer-list'),
    path("dashboard/lawyers/<int:pk>/", DeleteLawyerView.as_view(),name="delete-lawyer"),
    path("dashboard/create_user/", UserEditCreateView.as_view(),name="create_user"),
    path("appointment_detail/", appointment_detail , name="appointment_detail"),
    path('top-performers/', TopPerformersView.as_view(), name='top-performers'),


    
]

 
   