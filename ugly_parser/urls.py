from django.conf.urls import include, url
from django.contrib import admin
from ugly_parser.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^api/', include('site_reader.API.urls'))
    # url(r'^site_reader/', include('site_reader.urls')),
]
