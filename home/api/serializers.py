from rest_framework import serializers

from ..models import Dispatcher, Board, OwnerOperator, Driver, Invoice, InvoiceStatus


class DispatcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatcher
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class OwnerOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerOperator
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceStatus
        fields = '__all__'