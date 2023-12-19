from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import MHserializer
from rest_framework.response import Response
from web.models import qc_datasheet_mueller_hinton_agar




@api_view(['GET'])
def getRoutes(request):
        qc=qc_datasheet_mueller_hinton_agar.objects.all()
        serilaizer=MHserializer(qc,many=True)
        return Response(serilaizer.data)
