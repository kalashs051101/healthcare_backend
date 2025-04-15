from rest_framework import serializers
from .models import User, Patient, Doctor, PatientDoctorMapping
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class MappingSerializer(serializers.ModelSerializer):
    
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        # fields = '__all__'
        # fields = ['id', 'patient_name', 'doctor_name']
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name']
