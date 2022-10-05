from dataclasses import field
from rest_framework import serializers
from .models import Usermodel,Articlemodel

class UsermodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usermodel # 모델 설정
        fields = "__all__" # 필드 설정

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articlemodel
        fields = "__all__"
