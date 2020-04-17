from rest_framework import serializers
from .models import stockAPIData

class stockAPIDataSerializer (serializers.ModelSerializer):

    class Meta:
        model = stockAPIData
        fields = ('id','title','amount','unit','price','date',)
    
    def create(self, validated_data):
        return stockAPIData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.price = validated_data.get('price', instance.price)
        instance.date = validated_data.get('date', instance.date)

        instance.save()
        return instance




