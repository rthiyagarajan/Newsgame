from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('entity', views.EntityView)
router.register('qna', views.QNAView)
router.register('quiz', views.QuizView)


urlpatterns = [
    path('', include(router.urls))
]
