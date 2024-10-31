from djmoney.money import Money
from rest_framework import serializers

from products.models import Product, Type


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    price_amount = serializers.DecimalField(
        source='price.amount',
        max_digits=6,
        decimal_places=2
    )
    price_currency = serializers.CharField(
        source='price.currency',
        max_length=3
    )

    def create(self, validated_data):
        # Извлекаем значения цены и валюты из данных
        price_data = validated_data.pop('price')
        validated_data['price'] = Money(
            price_data['amount'],
            price_data['currency']
        )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Извлекаем значения цены и валюты из данных
        price_data = validated_data.pop('price', None)
        if price_data:
            instance.price = Money(
                price_data['amount'],
                price_data['currency']
                )
        return super().update(instance, validated_data)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price_amount',
            'price_currency',
            'amount',
            'barcode',
            'date_of_update',
            'type'
        ]
