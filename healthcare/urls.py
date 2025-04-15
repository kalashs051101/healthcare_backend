from django.urls import path
from healthcare.views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/register/', RegisterView.as_view()),

    path('api/patients/', PatientListCreateView.as_view()),
    path('api/patients/<int:pk>/', PatientDetailView.as_view()),

    path('api/doctors/', DoctorListCreateView.as_view()),
    path('api/doctors/<int:pk>/', DoctorDetailView.as_view()),

    path('api/mappings/', MappingListCreateView.as_view()),
    path('api/mappings/<int:pk>/', MappingDetailView.as_view()),
]
