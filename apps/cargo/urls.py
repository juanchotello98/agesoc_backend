from rest_framework import routers

from apps.cargo.viewsets import CargoViewSet

router = routers.SimpleRouter()
router.register('cargos', CargoViewSet)

urlpatterns = router.urls