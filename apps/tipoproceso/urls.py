from rest_framework import routers

from apps.tipoproceso.viewsets import TipoprocesoViewSet

router = routers.SimpleRouter()
router.register('tipoprocesos', TipoprocesoViewSet)

urlpatterns = router.urls