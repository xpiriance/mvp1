from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from user_chat.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login_data/', login_data),
    url(r'^', home_page),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
