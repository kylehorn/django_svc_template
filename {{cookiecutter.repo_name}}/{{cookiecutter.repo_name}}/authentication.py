from rest_framework import authentication, exceptions
from django.conf import settings


class ApplicationAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_APPLICATION_TOKEN')
        if token != settings.APPLICATION_AUTH_HEADER_TOKEN:
            raise exceptions.AuthenticationFailed('Access Denied')
