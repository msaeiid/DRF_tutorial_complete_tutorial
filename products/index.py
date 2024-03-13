from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex
from .models import Product

@register(Product)
class ProdcutIndex(AlgoliaIndex):
    # what ever method is or function is because of validation he used function
    should_index='is_public'

    fields=['user',
            'title',
            'content',
            'price',
            'public']
    

    tags='get_rags_list'