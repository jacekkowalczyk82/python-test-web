from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^mybacklog/', include('mybacklog.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),
]

