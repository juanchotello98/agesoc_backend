from rest_framework import routers

from apps.usuario.viewsets import UsuarioViewSet

router = routers.SimpleRouter()
router.register('usuarios', UsuarioViewSet)

urlpatterns = router.urls