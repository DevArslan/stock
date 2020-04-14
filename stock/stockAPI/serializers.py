from rest_framework import serializers
from .models import stockAPIData
from .models import resourcesData

# class RecursiveSerializer(serializers.Serializer):
#     def to_representation(self,value):
#         serializer = self.parent.parent.__class__(value, context = self.context)
#         return serializer.data

class stockAPIDataSerializer (serializers.ModelSerializer):

    class Meta:
        model = stockAPIData
        fields = ('Id','title','amount','unit','price','date',)
    
    def create(self, validated_data):
        return stockAPIData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Id = validated_data.get('Id', instance.Id)
        instance.title = validated_data.get('title', instance.title)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.price = validated_data.get('price', instance.price)
        instance.date = validated_data.get('date', instance.date)

        instance.save()
        return instance

class resourcesDataSerializer (serializers.ModelSerializer):
    # stock = RecursiveSerializer(many=True)
    # stock = stockAPIDataSerializer(many = True)
    # resourcesItem = stockAPIDataSerializer(many = True)
    class Meta:
        model = resourcesData
        fields = "__all__"

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     UserProfile.objects.create(user=user, **profile_data)
    #     return user

    def create(self, validated_data):
        resources_validated_data = validated_data.pop('stock')
        resource = resourcesData.objects.create(**validated_data)
        stockAPIData.objects.create(resource=resource, **resources_validated_data)
        return resource.data

