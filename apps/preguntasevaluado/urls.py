from rest_framework import routers

from apps.preguntasevaluado.viewsets import PreguntasevaluadoViewSet

router = routers.SimpleRouter()
router.register('preguntasevaluados', PreguntasevaluadoViewSet)

urlpatterns = router.urls