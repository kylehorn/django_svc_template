from {{cookiecutter.repo_name}}.authentication import ApplicationAuthentication
from rest_framework import status
from rest_framework import decorators
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.models import User


@decorators.api_view(['POST'])
@decorators.authentication_classes((ApplicationAuthentication,))
@decorators.permission_classes((AllowAny,))
def signup(request):
    serializer = serializers.SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(
            serializers.UserSerializer(
                user,
                context={'sign_up_request': request, 'sign_up': True}).data,
            status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_object(self):
        user = self.request.user
        if self.kwargs.get('pk') == 'self' and user:
            self.kwargs['pk'] = user.pk
            self.check_object_permissions(self.request, user)
            return user
        return super(UserViewSet, self).get_object()
