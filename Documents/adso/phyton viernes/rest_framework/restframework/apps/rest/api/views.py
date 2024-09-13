from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.rest.models import rest

class restApiView(APIView):
    def get(self,request):
        #rests = rest.object.all()
        rests = [rest.titulo for rest in rest.objects.all()]
        return Response(status=status.HTTP_200_OK,data='Hola mundo')