from rest_framework import serializers
from .models import Lecturer

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'firstName', 'middleName', 'surname', 'idNumber', 'email', 'phoneNumber', 'birthDate', 'created']