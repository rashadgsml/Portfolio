from django.contrib import admin
from django.urls import path

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core.views import index, detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('detail/<str:id>',detail,name='detail'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)