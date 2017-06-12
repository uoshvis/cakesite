from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework import permissions
from .serializers import MemberSerializer
from .models import Member
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class MemberViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    model = Member
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def list(self, request):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)
