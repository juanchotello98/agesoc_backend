from rest_framework import routers

from apps.respuestaencuesta.viewsets import RespuestaencuestaViewSet

router = routers.SimpleRouter()
router.register('respuestaencuestas', RespuestaencuestaViewSet)

urlpatterns = router.urls