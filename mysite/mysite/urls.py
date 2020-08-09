from django.contrib import admin
from django.urls import include, path
from polls.routes import router
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]