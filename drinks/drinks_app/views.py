from .models import Drinks
from .serializers import DrinkSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


@ api_view(['GET','POST'])
def drinks(request):

    if request.method == 'GET':
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response({"drinks":serializer.data})
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@ api_view(['GET','PUT','DELETE'])
def drink_detail(request,pk):
    try:
        drink = Drinks.objects.get(pk=pk)
    except Drinks.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = DrinkSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE" :
        drink.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)