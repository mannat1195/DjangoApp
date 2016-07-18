from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
	url(r'^appschedule/',include('appschedule.urls')),
    url(r'^admin/', admin.site.urls),
]
