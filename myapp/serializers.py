# serializers.py
from rest_framework import serializers
from .models import LeaveRequest  # Assure-toi que le modèle LeaveRequest existe dans models.py

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'  # Ou spécifie les champs manuellement ['start_date', 'end_date', ...]
