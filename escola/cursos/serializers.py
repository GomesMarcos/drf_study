from rest_framework import serializers

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


class CursoSerializer(serializers.ModelSerializer):
    # NESTED RELATIONSHIP -> Traz TODAS as informações do model que está sendo serializado
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # hiperlinked related field -> Traz um hiperlinque para as informações do model que está sendo serializado
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

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
        )