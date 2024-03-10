from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from rest_framework.request import Request
from . import validators
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url=serializers.HyperlinkedIdentityField(view_name='product_detail_update_delete',lookup_field='pk')
    title=serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)
    owner=UserPublicSerializer(read_only=True,source='user')
    edit_url=serializers.HyperlinkedIdentityField('update_view',lookup_field='pk')
    title=serializers.CharField(validators=[validators.title_unique_validator,validators.no_hi_in_title])

    class Meta:
        model = Product
        fields = [
                  'owner',
                  'url',
                  'edit_url',
                  'pk',
                  'title',
                  'content',
                  'price',
                  'sale_price',]

    

    def get_url(self,obj):
        #return f"v2/{obj.pk}" # first dummy way to send url to client, what if I change the url?
        #second way to send url, it's not bad...
        request=self.context.get('request')
        return reverse('product_detail_update_delete',kwargs={'pk':obj.pk},request=request)
