from rest_framework import routers, serializers, viewsets
import polls.viewsets as vs
import polls.views as v

router = routers.DefaultRouter()
router.register(r'municipios', vs.MunicipioViewSet)
router.register(r'capitanes', vs.CapitanViewSet)
router.register(r'lider', vs.LiderViewSet)
router.register(r'comuna', vs.ComunaViewSet)
router.register(r'puestos-de-votacion', vs.PuestosDeVotacionViewSet)
router.register(r'barrios', vs.BarrioViewSet)
router.register(r'datos-del-volante', vs.DatosDelVolanteViewSet)
router.register(r'lider-resp-barrio', vs.LiderRespBarrioViewSet)
router.register(r'cantidad-votantes', v.CantidadVotantes)
router.register(r'volantes-lider', v.VolantesLider)
router.register(r'votantes-municipios', v.VotantesMunicipios)
router.register(r'votantes-mesas', v.VotantesMesas)
