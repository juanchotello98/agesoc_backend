from rest_framework import routers

from apps.respuesta.viewsets import RespuestaViewSet

router = routers.SimpleRouter()
router.register('respuestas', RespuestaViewSet)

urlpatterns = router.urls