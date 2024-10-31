from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from products.models import Product, Type

from .serializers import ProductSerializer, TypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(
        methods=[
            'post',
            ],
        url_path='add_by_barcode',
        detail=False,
    )
    def add_by_barcode(self, request):
        """Добавление товара по штрихкоду. """
        barcode = request.data.get('barcode')
        if not barcode:
            return Response(
                {'error': 'Штрихкод не предоставлен'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            product = Product.objects.get(barcode=barcode)
            product.amount += 1
            product.save()

            return Response(
                {'status': f'Количество товара {product.name} увеличено',
                 'new_amount': product.amount},
                status=status.HTTP_200_OK
            )
        except Product.DoesNotExist:
            return Response(
                {'error': 'Товара с таким штрихкодом нет. Внесите в базу.'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(
        methods=[
            'get',
            ],
        url_path='subtract',
        detail=True,
    )
    def subtract(self, request, pk=None):
        """Уменьшение остатка товара. """
        product = get_object_or_404(Product, pk=pk)
        if product.amount > 0:
            product.amount -= 1
            product.save()
            return Response(
                {'status': f'Количество товара {product.name} уменьшено',
                 'new_amount': product.amount},
                status=status.HTTP_200_OK
            )
        else:
            # Если количество уже равно 0
            return Response(
                {'status': f'Недостаточно товара {product.name}',
                 'current_amount': product.amount},
                status=status.HTTP_400_BAD_REQUEST
            )


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
