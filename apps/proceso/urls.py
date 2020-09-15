from rest_framework import routers

from apps.proceso.viewsets import ProcesoViewSet

router = routers.SimpleRouter()
router.register('procesos', ProcesoViewSet)

urlpatterns = router.urls