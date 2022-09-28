from rest_framework import serializers
from .models import Usermodel

class UsermodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usermodel # 모델 설정
        fields = "__all__" # 필드 설정