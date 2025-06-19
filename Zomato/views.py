from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Product,Customer,Order,OrderItem
from .serializers import ProductSerializer,CustomerSerializer,OrderSerializer,OrderItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import ProductPagination , CustomerLimitOffsetPagination ,OrderItemCursorPagination ,OrderCursorPagination
from .throttling import ProductThrottle ,CustomerThrottle
from rest_framework.throttling import AnonRateThrottle
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.http import Http404
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class=ProductPagination
    throttle_classes=[AnonRateThrottle,ProductThrottle]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    pagination_class=CustomerLimitOffsetPagination
    throttle_classes=[AnonRateThrottle,CustomerThrottle]

class OrderList(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    pagination_class=OrderCursorPagination
    throttle_classes=[AnonRateThrottle,CustomerThrottle]

class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    lookup_field='pk'

class OrderItemList(generics.ListCreateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer
    pagination_class=OrderItemCursorPagination
    throttle_classes=[AnonRateThrottle,CustomerThrottle]
    permission_classes=[IsAuthenticated]

# class OrderItemDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset=OrderItem.objects.all()
#     serializer_class=OrderItemSerializer
#     lookup_field='pk'

class OrderItemDetails(APIView):
    def get_obj(self,pk):
        try:
            return OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist():
            raise Http404
    def get(self,req,pk):
        queryset=self.get_obj(pk)
        serializer=OrderItemSerializer(queryset)
        return Response(serializer.data)
    def put(self,req,pk):
        queryset=self.get_obj(pk)
        serializer=OrderSerializer(queryset,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,req,pk):
        queryset=self.get_obj(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
