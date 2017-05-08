from site_reader.models import NewsEntry
from rest_framework import serializers


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsEntry
        fields = ('title', 'author', 'url', 'site')