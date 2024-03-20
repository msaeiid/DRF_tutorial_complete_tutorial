from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex
from .models import Product


@register(Product)
class ProdcutIndex(AlgoliaIndex):
    # what ever method is or function is because of validation he used function
    # should_index='is_public'

    fields = ['user',
              'title',
              # by changing content to body it raises error
              'content',
              'price',
              'public',
              'path',
              'endpoint']

    settings = {
        # by changing content to body it raises error
        'searchableAttributes': ['title', 'content'],
        'attritubesForFaceting': ['user', 'public']
    }

    tags = 'get_rags_list'
