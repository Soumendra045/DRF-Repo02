from rest_framework import serializers
from .models import Product,Customer,Order,OrderItem

class ProductSerializer(serializers.ModelSerializer):
    length_name=serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields='__all__'
    
    def get_length_name(self,object):
        length=len(object.name)
        return length

    def validate_name(self, value):
        if value[0].isupper():            
            return value
        raise serializers.ValidationError("First letter should be chapital")
    def validate(self, attrs):
        price=attrs.get('price')
        if price <= 0:
            raise serializers.ValidationError("Price should not be Zero or less than Zero")
        return attrs

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
    def validate(self, attrs):
        name=attrs.get('name')
        if name[0].isupper():
            return attrs
        raise serializers.ValidationError("First letter of name should be capital")
    def validate_phoneNumber(self,value):
        if value[0] in ['0','1','2','3','4']:
            raise serializers.ValidationError("Phone number should not st with this")
        return value
    
class OrderSerializer(serializers.ModelSerializer):
    customer=serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    customer_details=CustomerSerializer(source='customer',read_only=True)
    # order=CustomerSerializer(many=True,read_only=True)
    class Meta:
        model=Order
        fields='__all__'

    

class OrderItemSerializer(serializers.ModelSerializer):
    order=serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    product=serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    order_details=OrderSerializer(source='order',read_only=True)
    product_details=ProductSerializer(source='product',read_only=True)
    class Meta:
        model=OrderItem
        fields='__all__'