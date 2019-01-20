from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        if request.query_params.get("all"):
            queryset = Product.objects.all()
        else:
            queryset = Product.objects.filter(inventory_count__gt=0)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def purchase(self, request, pk=None):
        product = self.get_object()
        try:
            product.purchase()
        except:
            return Response({"detail": "Cannot purchase a product not in stock"}, status=405)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


