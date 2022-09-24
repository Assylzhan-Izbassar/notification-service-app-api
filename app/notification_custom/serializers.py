from notification.serializers import ClientSerializer


class CustomClientSerializer(ClientSerializer):
    class Meta:
        fields = ['tag']