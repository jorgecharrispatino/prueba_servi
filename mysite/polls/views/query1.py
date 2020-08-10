from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import polls.models as m


class VolantesLider(APIView):

    def get(self, request, format=None):

        query = (m.Lider.objects
            .annotate(count=Count("datosdelvolante"))
            .values("nombre", "count"))
        return Response(query)