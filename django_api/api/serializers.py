from rest_framework import serializers
from base.models import Item, Origen1
from datetime import datetime



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CustomDateField(serializers.Field):
    """
    Custom field to handle date string in the format "dd/mm/yyyy".
    """

    def to_internal_value(self, data):
        try:
            return datetime.strptime(data, '%d/%m/%Y').date()
        except ValueError:
            raise serializers.ValidationError("Invalid date format. Use dd/mm/yyyy.")

    def to_representation(self, value):
        return value.strftime('%d/%m/%Y')

class Origen1Serializer(serializers.ModelSerializer):
    birthdate = CustomDateField()  # Use CustomDateField for birthdate
    full_name = serializers.CharField(source='get_full_name', read_only=True)  # Make full_name read-only
    origin = serializers.IntegerField(default=1, write_only=True)  # Add origin field

    class Meta:
        model = Origen1
        fields = '__all__'

    # def create(self, validated_data):
    #     full_name = f"{validated_data['name']} {validated_data['surnames']}"
    #     validated_data['full_name'] = full_name
    #     return super().create(validated_data)

class Origen2Serializer(serializers.ModelSerializer):
    birthdate = CustomDateField()  # Use CustomDateField for birthdate
    origin = serializers.IntegerField(default=2, write_only=True)  # Add origin field


    class Meta:
        model = Origen1
        fields = ('full_name', 'birthdate', 'amount')

