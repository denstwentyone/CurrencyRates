from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Currency, CurrencyRate
from .serializers import CurrencySerializer, CurrencyRateSerializer

import operator

class CurrencyList(APIView):
    def get(self, request, format=None):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        if request.method == 'POST':
            print(request.data)
            serializer = CurrencySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CurrencyRateList(APIView):
    def get(self, request, format=None):
        rates = CurrencyRate.objects.all()
        ordered_rates = sorted(rates, key=operator.attrgetter('date'))
        serializer = CurrencyRateSerializer(ordered_rates, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = CurrencyRateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)