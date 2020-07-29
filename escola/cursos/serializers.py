from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email' : { 'write_only' : True }, #write_only faz com que o parâmetro seja oculto. Ele é obrigatório apenas no momento do cadastro.
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'publicacao',
            'atualizacao',
            'is_ativo',
        )

    def validate_avaliacao(self, value):
        if value in range(1,6):
            return value
        raise serializers.ValidationError('A avaliação precisa ser um número inteiro entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # NESTED RELATIONSHIP -> Traz TODAS as informações do model que está sendo serializado
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # hiperlinked related field -> Traz um hiperlinque para as informações do model que está sendo serializado
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    media_avaliacoes = serializers.SerializerMethodField()

    # PRIMARY KEY RELATED FIELD -> Traz apenas o ID das informações do model que está sendo serializado
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'publicacao',
            'is_ativo',
            'avaliacoes',
            'media_avaliacoes',
        )
    
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2