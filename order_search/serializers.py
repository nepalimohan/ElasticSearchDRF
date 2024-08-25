from rest_framework import serializers

from . import models

class SalesOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SalesOrderItem
        fields = '__all__'
        

class SalesOrderSerializer(serializers.ModelSerializer):
    items = SalesOrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = models.SalesOrder
        fields = '__all__'