from rest_framework import serializers
from . models import Grup, Objec


class ObjecSerializer(serializers.ModelSerializer):
    grup = serializers.CharField()  # Используйте CharField для обработки имени группы

    class Meta:
        model = Objec
        fields = '__all__'

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        grup_name = data.get('grup')
        try:
            grup = Grup.objects.get(name=grup_name)
            ret['grup'] = grup.pk  # Используйте первичный ключ группы
        except Grup.DoesNotExist:
            raise serializers.ValidationError({"grup": "Grup with this name does not exist."})
        return ret


class GrupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grup
        fields = '__all__'

