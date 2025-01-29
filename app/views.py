from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HomeSerializer
from .models import Home
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


@api_view(['GET'])
def home(request):
    # fetch all the informations from the database
    items = Home.objects.all()

    #serialize the data to be seen i JSON format
    serializer = HomeSerializer(items, many=True)

    #return the serialized data 
    return Response(
        {
            "data": serializer.data
        }, status=HTTP_200_OK
    )


