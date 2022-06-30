from django.contrib import admin
from django.urls import path, include

from restapi.views import PressView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('api/press/', PressView.as_view(), name='press'), # press api 임시 추가(todo : db 연동)
    path('', include('urbanplay_clone_front.urls'))  # frontend urls.py 별도 관리
]
