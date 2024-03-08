from rest_framework.authentication import TokenAuthentication as BaseAuthentication


# change Token to Bearer when sending token
class TokenAuthentication(BaseAuthentication):
    keyword = 'Bearer'
