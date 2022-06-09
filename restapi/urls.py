from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('', include('urbanplay_clone_front.urls'))  # frontend urls.py 별도 관리
]
