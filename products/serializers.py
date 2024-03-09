from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from rest_framework.request import Request


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url=serializers.SerializerMethodField(read_only=True)
    #third way to send url, it's not bad...
    edit_url=serializers.HyperlinkedIdentityField('update_view',lookup_field='pk')

    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'sale_price', 'price', 'my_discount','url','edit_url']

    def get_my_discount(self, obj):
        if hasattr(obj, 'id'):
            return obj.get_discount()
        return None
    

    def get_url(self,obj):
        #return f"v2/{obj.pk}" # first dummy way to send url to client, what if I change the url?
        #second way to send url, it's not bad...
        request=self.context.get('request')
        return reverse('product_detail_update_delete',kwargs={'pk':obj.pk},request=request)
