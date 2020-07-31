import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from users.models import User

# with 'WSGIPathAuthorization On' if you are with server
# because aws automatically remove header


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                return None
            xjwt, jwt_token = token.split(" ")
            decode = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            pk = decode.get("pk")
            user = User.objects.get(pk=pk)
            return (user, None)
        except (ValueError, User.DoesNotExist):
            return None
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed(detail="JWT Format Invalid")
