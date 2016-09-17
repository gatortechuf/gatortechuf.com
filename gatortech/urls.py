from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('home.urls', namespace='home')),
    url(r'^calendar/', include('events.urls', namespace='events')),
    url(r'^resources/', include('resources.urls', namespace='resources')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
