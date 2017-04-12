from rest_framework.serializers import (
    EmailField,
    CharField,
    BooleanField,
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )
from django.contrib.auth.models import Permission
from rest_framework import serializers
from django.contrib.auth import get_user_model
from userModule.models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    ''' 
        profile serilizers.
    '''

    class Meta:
        model = Profile
        fields = ['location', 'phone']


class UserCreateSerializer(ModelSerializer):
    email    = EmailField(label='Email address')
    profile  = ProfileSerializer(required=False)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',  
            'is_staff',
            'profile',
        ]
        extra_kwargs = {'password':
                            {'write_only':True}
                        }

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get('email')
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError('This users has already registered')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username = username,
            email = email,
            is_staff= True
            
        )
        user_obj.set_password(password)
        user_obj.save()
        profile_data = validated_data#.pop('profile')
        user = User.objects.get(username=username)
        profile = Profile(user)
        user.profile.location = profile_data.get('location', profile.location)
        user.profile.phone = profile_data.get('phone', profile.phone)
        user.save()
        return validated_data

'''
    Override to return a custom response such as including the serialized representation of the User.
    Defaults to return the JWT token.
    Return tokon and user object (username & first_name)
'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name']

def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }


class UserListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='users-api:detail')
    delete_url = HyperlinkedIdentityField(view_name='users-api:user-delete')
    profile = ProfileSerializer(required=False, )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'url', 'delete_url', 'profile')


class UserUpdateSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='users-api:detail')
    delete_url = HyperlinkedIdentityField(view_name='users-api:user-delete')
    profile = ProfileSerializer(required=False, )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'url', 'delete_url', 'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        profile.location = profile_data.get('location', profile.location)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.save()

        return instance


# PERMISSIONS SERIALIZERS
class PermissionListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='users-api:permission-detail')
    class Meta:
        model = Permission
        fields = ('id','name','url','codename')


