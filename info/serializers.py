from rest_framework import serializers
from info.models import Info

class InfoSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    max_total_supply = serializers.IntegerField()

    def create(self, validated_data):
        return Info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.max_total_supply = validated_data.get('max_total_supply', instance.max_total_supply)
        instance.save()
        return instance