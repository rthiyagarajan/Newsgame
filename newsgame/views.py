from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Entity, QNA, Quiz
from .serializers import EntitySerializer, QNASerializer, QuizSerializer

class QNAView(viewsets.ModelViewSet):
    """
    Question and Answer (QNA) objects and linked Named Entities.
    None or multiple Entities can be linked to each QNA.
    Additional QNA objects can be created via POST by referencing the ID of the corresponding Entities:
    Example POST json:
    {
    "question":"",
    "answer":"",
    "entity":["1","2","3"]
    }
    """

    queryset = QNA.objects.all()
    serializer_class = QNASerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class EntityView(viewsets.ModelViewSet):
    """
    Named Entity objects.
    Additional Entity objects can be created one at a time via POST by assigning a name.
    The newEntity ID will be returned in the response.
    Example POST json:
    {
    "name":"Malcolm Turnbull"
    }
    """
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class QuizView(viewsets.ModelViewSet):
    """
    Quiz objects.
    Additional Quiz objects can be created via POST by assigning a name and referencing the ID of the corresponding QNA objects.
    At least 1 QNA ID must be linked.
    The new Quiz ID and linked QNA objects (including linked Entities) will be returned in the response.
    Example POST json:
    {
    "name":"Quiz 1"
    "qna":["3","4","5"]
    }
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
