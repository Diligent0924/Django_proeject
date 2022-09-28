from rest_framework import viewsets
from .serializer import UsermodelSerializer
from .models import Usermodel

class UsermodelSet(viewsets.ModelViewSet):
    queryset = Usermodel.objects.all()
    serializer_class = UsermodelSerializer
