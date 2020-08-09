from rest_framework import routers, serializers, viewsets
import polls.models as m

# Serializers define the API representation.


class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Municipio
        fields = ['id', 'nombre']


class CapitanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Capitan
        fields = ['id', 'nombre', 'apellido', 'celular']


class LiderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Lider
        fields = ['id', 'nombre', 'apellido', 'celular', 'capitan']


class ComunaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Comuna
        fields = ['id', 'name', 'municipio', 'capitanes']


class PuestosDeVotacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.PuestosDeVotacion
        fields = ['id', 'nombres', 'direccion', 'municipio']


class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Barrio
        fields = ['id', 'nombre', 'comuna']


class DatosDelVolanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.DatosDelVolante
        fields = [
            'id', 'nombres', 'apellidos', 'direccion',
            'telefono', 'cedula', 'mesa',
            'lider', 'barrio', 'puesto_votacion'
        ]


class LiderRespBarrioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.LiderRespBarrio
        fields = ['id', 'lider', 'capitan_comuna', 'barrio']
