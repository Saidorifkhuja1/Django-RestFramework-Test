from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .serializer import *
from rest_framework.permissions import *
from .permissions import *


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #authentication_classes = [TokenAuthentication]


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAdminOrReadOnly]




