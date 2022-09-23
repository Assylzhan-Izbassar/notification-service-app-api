"""
Creating views for notification models.
"""
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Distribution, Client, Message
from .serializers import DistributionSerializer, ClientSerializer, MessageSerializer


class DistributionViewSet(ModelViewSet):
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if Message.objects.filter(client_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Client cannot be deleted because it has message(s).'})
        return super().destroy(request, *args, **kwargs)


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_serializer_context(self):
        return {'request': self.request}
