from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .utils.security.check_user_groups import IsUserGroup, IsAdminGroup


class User(APIView):

    permission_classes = [IsAuthenticated, IsUserGroup]

    @extend_schema(tags=["API"])
    def get(self, request):
        return Response({'message': 'Hello, world!'}, status=status.HTTP_200_OK)

class Admin(APIView):

    permission_classes = [IsAuthenticated, IsAdminGroup]

    @extend_schema(tags=["API"])
    def get(self, request):
        return Response({'message': 'Hello, world!'}, status=status.HTTP_200_OK)
