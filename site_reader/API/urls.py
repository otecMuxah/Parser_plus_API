from django.conf.urls import url, include
from rest_framework import routers
from site_reader.API.views import NewsViewSet, FilteredList

router = routers.DefaultRouter()
router.register(r'posts', NewsViewSet)
# router.register(r'^posts/(?P<site>.*)/$', FilteredList.as_view())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^posts/(?P<site>.+)/$', FilteredList.as_view()),
]
