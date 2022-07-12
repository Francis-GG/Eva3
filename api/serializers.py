from rest_framework import serializers
from frontend.models import producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'