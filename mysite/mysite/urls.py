from django.contrib import admin
from django.urls import include, path
from polls.routes import router
from django.conf.urls import url
import polls.views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r"cantidad-votantes", v.CantidadVotantes.as_view()),
    url(r"volantes-lider", v.VolantesLider.as_view()),
    url(r"votantes-municipios", v.VotantesMunicipios.as_view()),
    url(r"votantes-mesas", v.VotantesMesas.as_view()),
]