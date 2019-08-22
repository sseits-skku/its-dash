from django.contrib.auth.models import AnonymousUser
from rest_framework import exceptions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication as JWTAuth


def jwt_auth_middleware(get_response):
    """Sets the user object from a JWT header"""
    def middleware(request):
        try:
            authenticated = JWTAuth().authenticate(request)
            if authenticated:
                request.user = authenticated[0]
            else:
                request.user = AnonymousUser
        except exceptions.AuthenticationFailed as err:
            print(err)
            request.user = AnonymousUser

        response = get_response(request)

        return response

    return middleware
