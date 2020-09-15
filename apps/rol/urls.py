from rest_framework import routers

from apps.rol.viewsets import RolViewSet

router = routers.SimpleRouter()
router.register('roles', RolViewSet)

urlpatterns = router.urls