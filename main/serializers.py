from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Currency, CurrencyRate

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            "id",
            "name",
        )

class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = (
            "id",
            "currency",
            "date",
            "rate",
        )