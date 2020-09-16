from rest_framework import routers

from apps.pregunta.viewsets import PreguntaViewSet

router = routers.SimpleRouter()
router.register('preguntas', PreguntaViewSet)

urlpatterns = router.urls