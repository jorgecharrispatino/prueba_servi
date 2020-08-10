from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import polls.models as m


class CantidadVotantes(APIView):

    def get(self, request, format=None):

        query = (m.DatosDelVolante.objects.count())
        return Response(query)