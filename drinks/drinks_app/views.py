from .models import Drinks
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

# using mixins
class DrinksGenericView(generics.GenericAPIView,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Drinks.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request, id=id)
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    def put(self,request, id=None):
        return self.update(request,id=id)
    
    def delete(self,request,id=None):
        return self.destroy(request, id=id)

# using class based apiviews
class DrinksAPIView(APIView):
    def get(self,request):
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response({"drinks":serializer.data})
    
    def post(self,request):
        serializer = DrinkSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class drink_detailAPIView(APIView):
    def get_object(self,pk):
        try:
            return Drinks.objects.get(pk=pk)
        except Drinks.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        drink = self.get_object(pk)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    def put(self,request,pk):
        drink = self.get_object(pk)
        serializer = DrinkSerializer(drink, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        drink = self.get_object(pk)
        drink.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# using apiview
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
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = DrinkSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE" :
        drink.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)