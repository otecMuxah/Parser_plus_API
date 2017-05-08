import django_filters.rest_framework
from rest_framework import viewsets
from site_reader.API.serializers import NewsSerializer
from site_reader.models import NewsEntry
from rest_framework import generics


class NewsViewSet(viewsets.ModelViewSet):

    queryset = NewsEntry.objects.all()
    serializer_class = NewsSerializer


