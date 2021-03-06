from rest_framework import generics
from rest_framework.generics import get_object_or_404

""" V2 """
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import IsSuperUser

"""
API V1
"""


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

    def query_set(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

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

    def get_object(self):
        if self.kwargs.get('cursp_pk'):
            return get_object_or_404(   self.get_queryset(),
                                        curso_id=self.kwargs.get('curso_pk'),
                                        pk=self.kwargs.get('avaliacao_pk')
                                    )
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""
class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsSuperUser, #Se a situação nessa classe for resolvida (tiver algum return), as classes abaixo são ignoradas
        permissions.DjangoModelPermissions,
    )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):

        #PAGINANDO AVALIAÇÕES DENTRO DE CURSOS PARA 1
        self.pagination_class.page_size = 1 
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)
""" 
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""

# Para não permitir deletar, basta comentar o mixins.DestroyModelMixin,
class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

