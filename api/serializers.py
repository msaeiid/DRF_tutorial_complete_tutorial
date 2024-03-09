from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    url=serializers.HyperlinkedIdentityField(view_name='product_detail_update_delete',lookup_field='pk')
    title=serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username=serializers.CharField(read_only=True)
    id=serializers.IntegerField(read_only=True)
    other_products=serializers.SerializerMethodField(read_only=True)

    def get_other_products(self,obj):
        user=obj
        user_product=user.product_set.all()
        return UserProductInlineSerializer(instance=user_product,many=True,context=self.context).data