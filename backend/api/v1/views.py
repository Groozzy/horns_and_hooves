from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from api.v1 import filters, permissions, serializers
from carts.models import Cart
from orders.models import Order
from products.models import Product


class ProductRetrieveViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsStaffOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.ProductFilter


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductFilterAPIView(APIView):
    def post(self, request):
        data = request.data
        categories = data.get('categories', [])
        products = Product.objects.filter(categories__in=categories)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    permissions = (permissions.IsOwner,)
    serializer_class = serializers.CartSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
