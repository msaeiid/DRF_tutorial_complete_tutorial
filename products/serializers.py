from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from rest_framework.request import Request
from . import validators


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url=serializers.SerializerMethodField(read_only=True)
    ## only for Model Serializer Create & Update Methods added
    #email=serializers.EmailField(write_only=True)
    #third way to send url, it's not bad...
    edit_url=serializers.HyperlinkedIdentityField('update_view',lookup_field='pk')
    title=serializers.CharField(validators=[validators.title_unique_validator,validators.no_hi_in_title])
    #email=serializers.CharField(source='user.email',read_only=True)## same as related in odoo for FK is working

    class Meta:
        model = Product
        fields = ['id',
                  ## only for Model Serializer Create & Update Methods added
                  #'email',
                  'title',
                  #'name',
                  'content',
                  'sale_price',
                  'price',
                  'my_discount',
                  'url',
                  'edit_url']
    ## there are two ways for validating a field in serializer, in seprate file and validate in serializer or on model    
    #def validate_<fieldname> not for read_only and validate in update, create ,...
    # def validate_title(self,value):
    #     request=self.context.get('request')
    #     user=request.user
    #     #is_exist = Product.objects.filter(title__iexact=value,user=user).exists()
    #     is_exist = Product.objects.filter(title__iexact=value).exists()
    #     if is_exist:
    #         raise serializers.ValidationError(f"{value} is aleady a product name")
    #     else:
    #         return value

    def get_my_discount(self, obj):
        if hasattr(obj, 'id'):
            return obj.get_discount()
        return None
    ## only for Model Serializer Create & Update Methods added
    # def create(self, validated_data):
    #     email=validated_data.pop('email')
    #     return super().create(validated_data)   
    
    ## only for Model Serializer Create & Update Methods added
    # def update(self, instance, validated_data):
    #     email=validated_data.pop('email')
    #     return super().update(instance, validated_data)
    

    def get_url(self,obj):
        #return f"v2/{obj.pk}" # first dummy way to send url to client, what if I change the url?
        #second way to send url, it's not bad...
        request=self.context.get('request')
        return reverse('product_detail_update_delete',kwargs={'pk':obj.pk},request=request)
