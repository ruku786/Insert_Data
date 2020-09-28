from rest_framework import viewsets
from . import models
from . import serializers


class employeeViewset(viewsets.ModelViewSet):
    queryset = models.employee.objects.all()
    serializer_class = serializers.employeeSerializer
