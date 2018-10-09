from rest_framework import serializers
from .models import QNA, Entity, Quiz

class EntitySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Entity
        fields = ('id', 'url', 'name')

class QNASerializer(serializers.HyperlinkedModelSerializer):
    
    # Allow POST using Entity object ID "entity":["1","3"]
    # entity will not be visible in the API response due to write_only
    entity = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Entity.objects.all(), many=True)
    # Nested Serializer to display all the linked Entitys
    entity_info = EntitySerializer(source='entity', read_only=True, many=True)

    class Meta:
        model = QNA
        fields = ('id', 'url', 'question', 'answer', 'entity', 'entity_info')

class QuizSerializer(serializers.HyperlinkedModelSerializer):

    qna = serializers.PrimaryKeyRelatedField(write_only=True, queryset=QNA.objects.all(), many=True)    

    #Nested Serializer to display all the QNA info (including assigned Entity)
    qna_info = QNASerializer(source='qna', many=True, read_only=True)
    class Meta:
        model = Quiz
        #read_only_fields = ('id', 'QNA_name')
        fields = ('id', 'url', 'name','qna', 'qna_info')
