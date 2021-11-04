from app1.models import Product, Order, Item
from app1.serializers import ProductSerializer, OrderSerializer
from app1.utils import get_random_value
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import json


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(data=serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(data=serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def order(request, id):
    if request.method == 'GET':
        try:
            order = Order.objects.get(id=id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
        serializer = OrderSerializer(order, many=False)
        return Response(data=serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_order(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            order_id = body['order_id']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.get(id=order_id)
        if order.ordered:
            return Response(data=json.dumps({"Mensaje": "El pedido ya ha sido tramitado"}))
        shipping_price = get_random_value(min_value=3, max_value=10)
        order.shipping_charges = shipping_price
        order.ordered = True
        order.save()
        serializer = OrderSerializer(order, many=False)
        return Response(data=serializer.data)
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_item(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            product_id = body['product_id']
            quantity = body['quantity']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.get(id=product_id)
        item = Item.objects.create(product=product, quantity=quantity)

        if "order_id" in body:
            order = Order.objects.get(id=body['order_id'])
        else:
            order = Order.objects.create(user=request.user)
        
        order.items.add(item)
        order.save()
        serializer = OrderSerializer(order, many=False)
        return Response(data=serializer.data)
