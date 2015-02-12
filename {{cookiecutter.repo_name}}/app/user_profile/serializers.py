from django.contrib.auth.models import User
from rest_framework import serializers
from {{cookiecutter.repo_name}}.serializers import ShortListSerializerMixin, \
    DynamicFieldsModelSerializer


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(ShortListSerializerMixin, DynamicFieldsModelSerializer):
    full_name = serializers.CharField(
        source='get_full_name', read_only=True)
    email = serializers.EmailField(required=True)
    created_at = serializers.DateTimeField(
        source='date_joined', read_only=True, required=False)
    is_active = serializers.BooleanField(
        read_only=True, source='profile.is_active')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'full_name', 'created_at', 'password', 'is_active')
        write_only_fields = ('password',)
        list_fields = ('id', 'username', 'full_name', 'is_active')
