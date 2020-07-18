from rest_framework import generics

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursosAPIView(generics.ListCreateAPIView):
    """ 
    API DE CURSOS
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    """ 
    API DE AVALIAÇÕES
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ 
    API SINGLE DE CURSOS
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ 
    API SINGLE DE AVALIAÇÕES
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer