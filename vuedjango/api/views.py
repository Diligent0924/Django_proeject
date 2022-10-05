# from urllib import request
from urllib import request
from rest_framework.viewsets import ModelViewSet
from .serializer import UsermodelSerializer, ArticleSerializer
from .models import Usermodel, Articlemodel
from rest_framework.response import Response

class UsermodelSet(ModelViewSet):
    queryset = Usermodel.objects.all()
    serializer_class = UsermodelSerializer


class ArticleSet(ModelViewSet):
    queryset = Articlemodel.objects.all()
    serializer_class = ArticleSerializer