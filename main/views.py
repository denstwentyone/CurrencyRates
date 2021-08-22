from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Currency, CurrencyRate
from .serializers import CurrencySerializer, CurrencyRateSerializer

class CurrencyList(APIView):
    def get(self, request, format=None):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        return Response("ok")
        
class CurrencyRateList(APIView):
    def get(self, request, format=None):
        rates = CurrencyRate.objects.all()
        serializer = CurrencyRateSerializer(rates, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        if request.method == 'POST':
            print(request.data)
            serializer = CurrencyRateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
