from rest_framework import routers, serializers, viewsets
import polls.models as m
import polls.serializers as s

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = m.Municipio.objects.all()
    serializer_class = s.MunicipioSerializer

class CapitanViewSet(viewsets.ModelViewSet):
    queryset = m.Capitan.objects.all()
    serializer_class = s.CapitanSerializer

class LiderViewSet(viewsets.ModelViewSet):
    queryset = m.Lider.objects.all()
    serializer_class = s.LiderSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = m.Comuna.objects.all()
    serializer_class = s.ComunaSerializer

class PuestosDeVotacionViewSet(viewsets.ModelViewSet):
    queryset = m.PuestosDeVotacion.objects.all()
    serializer_class = s.PuestosDeVotacionSerializer

class BarrioViewSet(viewsets.ModelViewSet):
    queryset = m.Barrio.objects.all()
    serializer_class = s.BarrioSerializer

class DatosDelVolanteViewSet(viewsets.ModelViewSet):
    queryset = m.DatosDelVolante.objects.all()
    serializer_class = s.DatosDelVolanteSerializer

class LiderRespBarrioViewSet(viewsets.ModelViewSet):
    queryset = m.LiderRespBarrio.objects.all()
    serializer_class = s.LiderRespBarrioSerializer