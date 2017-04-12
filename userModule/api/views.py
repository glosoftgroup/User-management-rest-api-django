from django.db.models import Q

from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    )

from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     RetrieveUpdateAPIView)
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import Permission

from .serializers import (
    UserListSerializer,
    UserCreateSerializer,
    PermissionListSerializer,
    UserUpdateSerializer
     )
from rest_framework import generics


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()


# class UserCreateAPIView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer
#
#     def perform_create(self, serializer):
#         #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         serializer.save(user=self.request.user)


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer



class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all().select_related('profile')
    serializer_class = UserListSerializer


class UpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all().select_related('profile')
    serializer_class = UserUpdateSerializer
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# Permissions views
class PermissionListView(generics.ListAPIView):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all()


class PermissionDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all()








