from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'sale_price', 'price', 'my_discount']

    def get_my_discount(self, obj):
        if hasattr(obj, 'id'):
            return obj.get_discount()
        return None
