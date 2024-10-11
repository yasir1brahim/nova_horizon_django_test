# serializers.py
from rest_framework import serializers
from .models import AccountStage

class AccountStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStage
        fields = '__all__'  # or specify the fields you want
