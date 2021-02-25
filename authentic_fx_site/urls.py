from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentic_fx.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),
]
